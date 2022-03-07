from django.shortcuts import render
from django.http import HttpResponse


from structure.models import Structure, Chain, StructureDomain, PDBData

def index(request):
    return HttpResponse("Hello, world. This is SH2db structure page.")

def structure(request, pdb_code):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
    except Structure.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'structure.html', {'structure' : structure})
    
def chain(request, pdb_code, chain_ID):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
        chain = Chain.objects.get(structure=structure, chain_ID=chain_ID)
    except Chain.DoesNotExist:
        return render(request, 'error.html')
        
    return render(request, 'chain.html', {'chain' : chain})
    
def structuredomain(request, pdb_code, domaintype, chain_ID):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
        chain = Chain.objects.get(structure=structure, chain_ID=chain_ID)
        structuredomains = StructureDomain.objects.filter(chain=chain)

        for i in structuredomains:
            if i.domain.domain_type.slug == domaintype:
                structuredomain = i
    except Chain.DoesNotExist:
        return render(request, 'error.html')
        
    return render(request, 'structuredomain.html', {'structuredomain' : structuredomain})
