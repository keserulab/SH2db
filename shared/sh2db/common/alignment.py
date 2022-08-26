from residue.models import Residue
from protein.models import ProteinSegment

class Alignment():
    def __init__(self, domains):
        self.domains = domains

    def align_domain_residues(self):
        residues = []
        for d in self.domains:
            residues.append(Residue.objects.filter(domain=d).prefetch_related('protein_segment'))
        segments = {}
        gns = {}
        segs_to_keep = []
        for resis in residues:
            segs = ProteinSegment.objects.all()
            for seg in segs:
                resis_in_seg = resis.filter(protein_segment=seg)
                if seg not in gns:
                    gns[seg] = []
                for res in resis_in_seg:
                    if not res.generic_number:
                        if len(resis_in_seg)>len(gns[seg]):
                            gns[seg] = [''] * len(resis_in_seg)
                            break
                    elif res.generic_number.label not in gns[seg]:
                        gns[seg].append(res.generic_number.label)
                gns[seg] = sorted(gns[seg])
                if len(gns[seg])>0:
                    segs_to_keep.append(seg)
        for seg in list(gns.keys()-segs_to_keep):
            del gns[seg]

        gns_out = []
        for seg, gns_list in gns.items():
            if gns_list[0]!='':
                gns_list = [int(i[-2:]) for i in gns_list]
                gns_out += [str(i) for i in sorted(gns_list)]
            else:
                gns_out += gns_list
            segments[seg] = len(gns_list)

        aligned_domains = []
        for resis in residues:
            if resis[0].domain.parent:
                aligned_residues = [resis[0].domain.isoform.protein.name,resis[0].domain]
            else:
                aligned_residues = [resis[0].domain.isoform.protein.name,resis[0].domain.domain_type]
            for seg in segments:
                seg_resis = resis.filter(protein_segment=seg)
                if seg.fully_aligned:
                    for gn in gns[seg]:
                        try:
                            aligned_residues.append(resis.get(generic_number__label=gn))
                        except Residue.DoesNotExist:
                            aligned_residues.append('-')
                elif seg.slug=='N-term':
                    for i, gn in enumerate(gns[seg]):
                        if len(gns[seg][i:])-len(seg_resis)>0:
                            aligned_residues.append('-')
                        else:
                            aligned_residues.append(resis[i-(len(gns[seg])-len(seg_resis))])
                elif seg.slug=='C-term':
                    for i, gn in enumerate(gns[seg]):
                        try:
                            aligned_residues.append(seg_resis[i])
                        except IndexError:
                            aligned_residues.append('-')
                else:
                    for i, gn in enumerate(gns[seg]):
                        # if len(seg_resis)!=len(gns[seg]):
                        #     if len(seg_resis)/2<i:
                        #         aligned_residues.append(seg_resis[i])
                        #     elif 
                        # else:
                        #     aligned_residues.append(seg_resis[i])
                        try:
                            aligned_residues.append(seg_resis[i])
                        except IndexError:
                            aligned_residues.append('-')

            aligned_domains.append(aligned_residues)

        

        return segments, gns_out, aligned_domains