from django.shortcuts import render
from django.http import HttpResponse


from structure.models import Structure, Chain, StructureDomain

def index(request):
    return HttpResponse("Hello, world. This is SH2db structure page.")

def structure(request, pdb_code):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
        chains = Chain.objects.filter(structure=structure)
        structuredomains = StructureDomain.objects.filter(chain__structure=structure)

        protein = structuredomains[0].domain.isoform.protein

    except Structure.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'structure.html', {'structure' : structure, 'chains': chains, 'structuredomains' : structuredomains, 'protein': protein})
    
def chain(request, pdb_code, chain_ID):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
        chain = Chain.objects.get(structure=structure, chain_ID=chain_ID)
        structuredomains = StructureDomain.objects.filter(chain=chain)

        protein = structuredomains[0].domain.isoform.protein
    except Chain.DoesNotExist:
        return render(request, 'error.html')
        
    return render(request, 'chain.html', {'structure' : structure, 'chain' : chain, 'structuredomains' : structuredomains, 'protein': protein})
    
def structuredomain(request, pdb_code, domaintype, chain_ID):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
        chain = Chain.objects.get(structure=structure, chain_ID=chain_ID)
        structuredomains = StructureDomain.objects.filter(chain=chain)

        protein = structuredomains[0].domain.isoform.protein

        for i in structuredomains:
            if i.domain.domain_type.slug == domaintype:
                structuredomain = i
    except Chain.DoesNotExist:
        return render(request, 'error.html')
        
    return render(request, 'structuredomain.html', {'structure' : structure, 'chain' : chain, 'structuredomain' : structuredomain, 'protein': protein})
