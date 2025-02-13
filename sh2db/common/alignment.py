from residue.models import Residue
from protein.models import ProteinSegment
from datetime import datetime


class Alignment():
    def __init__(self, domains):
        self.domains = domains

    def align_domain_residues(self):
        start = datetime.now()
        residues = []
        for d in self.domains:
            residues.append(Residue.objects.filter(domain=d))#.prefetch_related('protein_segment','generic_number','domain__isoform__protein','domain__domain_type'))
        print('fetch residues', datetime.now()-start)
        segments, segment_gns = {}, {}
        gns = {}
        segs_to_keep = []
        segs = ProteinSegment.objects.all()
        for resis in residues:
            for seg in segs:
                resis_in_seg = resis.filter(protein_segment=seg)
                if seg not in gns:
                    gns[seg] = []
                for res in resis_in_seg:
                    if seg.slug=='bBbC':
                        if res.generic_number:
                            if res.generic_number.label not in gns[seg]:
                                gns[seg].append(res.generic_number.label)
                        elif len(resis_in_seg)>len(gns[seg]):
                            gns[seg].append('')
                    elif not res.generic_number:
                        if len(resis_in_seg)>len(gns[seg]):
                            gns[seg] = [''] * len(resis_in_seg)
                            break
                    elif res.generic_number.label not in gns[seg]:
                        gns[seg].append(res.generic_number.label)
                if len(gns[seg])>0:
                    segs_to_keep.append(seg)
        for seg in list(gns.keys()-segs_to_keep):
            del gns[seg]
        for seg, val in gns.items():
            if seg.slug!='bBbC':
                gns[seg] = sorted(val)
        print('gns check', datetime.now()-start)
        gns_out = []
        for seg, gns_list in gns.items():
            if seg.slug=='bBbC':
                mod_gns_list = []
                for i in gns_list:
                    if i!='':
                        gns_out.append(i.split('x')[1])
                        mod_gns_list.append(int(i.split('x')[1]))
                    else:
                        gns_out.append('')
                        mod_gns_list.append('')
                gns_list = mod_gns_list
            elif gns_list[0]!='':
                gns_list = [int(i.split('x')[1]) for i in gns_list]
                gns_out += [str(i) for i in gns_list]
            else:
                gns_out += gns_list
            segments[seg] = len(gns_list)
            segment_gns[seg] = gns_list
        print('segments', datetime.now()-start)
        aligned_domains = []
        for resis in residues:
            if resis[0].domain.parent:
                aligned_residues = [resis[0].domain.isoform.protein,resis[0].domain]
            else:
                aligned_residues = [resis[0].domain.isoform.protein,resis[0].domain.domain_type]
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
        print('alignment', datetime.now()-start)
        sheinerman = []
        offset = 0
        sheinerman_dict = {'aA':[43,47], 'bB':[50,52], 'bBbC':[49,50], 'bD':[50,52]}
        for seg, gns in segment_gns.items():
            if seg.slug in sheinerman_dict:
                for i in sheinerman_dict[seg.slug]:
                    if i in gns:
                        sheinerman.append(offset+gns.index(i))
            offset+=len(gns)
        print('sheinerman', datetime.now()-start)

        return segments, gns_out, aligned_domains, sheinerman
