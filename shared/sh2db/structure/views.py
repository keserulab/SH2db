from django.shortcuts import render
from django.http import HttpResponse


from structure.models import Structure, Chain, StructureDomain

def index(request):
    return HttpResponse("Hello, world. This is SH2db structure page.")

def structure(request, pdb_code):
    try:
        structure = Structure.objects.get(name=name)
    except Structure.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'protein.html', {'domains' : domains,  'structuredomains': structuredomains, 'protein': protein, 'fullname': fullname})
    return HttpResponse("Hello, world. This is the protein page for %s." % pdb_code)
    
def chain(request, pdb_code, chain_ID):
    return HttpResponse("Hello, world. This is the Chain page for %s, %s." % (pdb_code, chain_ID) )
    
def domain(request, pdb_code, domain, chain_ID):
    return HttpResponse("Hello, world. This is the StructureDomain page for %s, %s, %s." % (pdb_code, chain_ID, domain) )