from django.shortcuts import render
from django.http import HttpResponse

from protein.models import Protein, Domain


import requests
import xml.etree.ElementTree as ET


def index(request):
    return HttpResponse("Hello, world. This is SH2db protein page.")

def protein(request, name):
    protein = Protein.objects.get(name=name)
    
    res=requests.get('https://www.uniprot.org/uniprot/'+protein.accession+'.xml')
    root = ET.fromstring(res.content)
    entry = root.findall('{http://uniprot.org/uniprot}entry')[0]
    fullname = entry.findall('{http://uniprot.org/uniprot}protein')[0].findall('{http://uniprot.org/uniprot}recommendedName')[0].findall('{http://uniprot.org/uniprot}fullName')[0].text
    
    domains = Domain.objects.filter(isoform_id=protein.id)
    
    return render(request, 'protein.html', {'domains' : domains, 'protein': protein, 'fullname': fullname})#, 'headers' : headers})