from django.shortcuts import render
from django.http import HttpResponse

from protein.models import Protein, Isoform, Domain
from structure.models import StructureDomain


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
    
    domains = Domain.objects.filter(isoform__protein=protein, parent__isnull=True)

    structuredomains = StructureDomain.objects.filter(domain__isoform__protein=protein)
    
    return render(request, 'protein.html', {'domains' : domains,  'structuredomains': structuredomains, 'protein': protein, 'fullname': fullname})
