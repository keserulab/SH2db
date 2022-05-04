from django.shortcuts import render

from django.http import HttpResponse

from protein.models import Protein, Domain, ProteinSegment
from residue.models import Residue, ResidueGenericNumber
from common.alignment import Alignment


def index(request):
    return render(request, 'index.html')

def search(request):
    domains = Domain.objects.all().order_by('isoform', 'domain_type', '-parent', 'name')

    proteinsegments = ProteinSegment.objects.all()
    residuegenericnumbers = ResidueGenericNumber.objects.all()
    residues = Residue.objects.filter(domain__in=domains)

    alignment = Alignment(domains)
    segments, gns, residues = alignment.align_domain_residues()
    
    

    return render(request, 'search.html', { 'domains': domains,
                                            'proteinsegments': proteinsegments, 'residuegenericnumbers': residuegenericnumbers, 'residues': residues,
                                            'gns': gns, 'segments': segments, 'checkbox': True, 'filter':True})
    

def browse(request):

    headers = ["Family", "Gene name", "Species", "Uniprot"]
    
    data = Protein.objects.all()
    
    return render(request, 'browse.html', {'data' : data, 'headers' : headers})

def charts(request):
    return render(request, 'charts.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

