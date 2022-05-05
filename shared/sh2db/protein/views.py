from django.shortcuts import render
from django.http import HttpResponse

from protein.models import Protein, Isoform, Domain, ProteinSegment
from structure.models import Structure, StructureDomain
from residue.models import Residue
from common.alignment import Alignment


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

    alignment = Alignment(domains)
    segments, gns, residues = alignment.align_domain_residues()

    structures = []
    for s in structuredomains:
        if s.chain.structure not in structures:
            structures.append(s.chain.structure)

    return render(request, 'protein.html', {'domains' : domains,  'structures': structures, 'protein': protein, 'fullname': fullname, 'residues': residues, 'segments': segments, 'gns': gns})
