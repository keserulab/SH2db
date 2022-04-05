from django.shortcuts import render
from django.http import HttpResponse

from protein.models import Protein, Isoform, Domain, ProteinSegment
from structure.models import Structure, StructureDomain
from residue.models import Residue


import requests
import xml.etree.ElementTree as ET


def index(request):
    return HttpResponse("Hello, world. This is SH2db protein page.")

def protein(request, name):

    try:
        protein = Protein.objects.get(name=name)
    except Protein.DoesNotExist:
        return render(request, 'error.html')
    
    # Get current full name by looking up UniProt entry
    res=requests.get('https://www.uniprot.org/uniprot/'+protein.accession+'.xml')
    root = ET.fromstring(res.content)
    entry = root.findall('{http://uniprot.org/uniprot}entry')[0]
    fullname = entry.findall('{http://uniprot.org/uniprot}protein')[0].findall('{http://uniprot.org/uniprot}recommendedName')[0].findall('{http://uniprot.org/uniprot}fullName')[0].text
    
    domains = Domain.objects.filter(isoform__protein=protein, parent__isnull=True).order_by('-domain_type__slug')

    structuredomains = StructureDomain.objects.filter(domain__isoform__protein=protein)

    
    segments, gns, residues = align_domain_residues(domains)

    structures = []
    for s in structuredomains:
        if s.chain.structure not in structures:
            structures.append(s.chain.structure)

    return render(request, 'protein.html', {'domains' : domains,  'structures': structures, 'protein': protein, 'fullname': fullname, 'residues': residues, 'segments': segments, 'gns': gns})

def align_domain_residues(domains):
    residues = []
    for d in domains:
        residues.append(Residue.objects.filter(domain=d))
    segments = {}
    gns = {}
    for resis in residues:
        segs = resis.order_by('protein_segment__id').distinct('protein_segment').values_list('protein_segment__slug', flat=True)
        for seg in segs:
            resis_in_seg = resis.filter(protein_segment__slug=seg)
            seg = resis_in_seg[0].protein_segment
            if seg not in segments:
                segments[seg] = len(resis_in_seg)
            else:
                if len(resis_in_seg)>segments[seg]:
                    segments[seg] = len(resis_in_seg)
            if seg not in gns:
                gns[seg] = []
            for res in resis_in_seg:
                if not res.generic_number:
                    if len(resis_in_seg)>len(gns[seg]):
                        gns[seg] = [''] * len(resis_in_seg)
                        break
                elif res.generic_number.label not in gns[seg]:
                    gns[seg].append(res.generic_number.label)

    gns_out = []
    for seg, gns_list in gns.items():
        if gns_list[0]!='':
            gns_list = [int(i[-2:]) for i in gns_list]
            gns_out += [str(i) for i in sorted(gns_list)]
        else:
            gns_out += gns_list

    aligned_domains = []
    for resis in residues:
        aligned_residues = [resis[0].domain.domain_type.name]
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
                        print(i, seg_resis[i])
                        aligned_residues.append(seg_resis[i])
                    except IndexError:
                        aligned_residues.append('-')


        aligned_domains.append(aligned_residues)

    

    return segments, gns_out, aligned_domains





