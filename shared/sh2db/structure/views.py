from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string



from structure.models import Structure, Chain, StructureDomain
from residue.models import Residue, ResidueGenericNumber
from protein.models import ProteinSegment

import StringIO

def index(request):
    return HttpResponse("Hello, world. This is SH2db structure page.")
    
def zipped_pdb(request, structuredomains):
    mf = StringIO.StringIO()
    with zipfile.ZipFile(mf, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for structuredomain in structuredomains:
            zf.writestr(structuredomain.domain.name+'.txt', structuredomain.pdbdata)

    #Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), mimetype = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zf
    return resp

def structure(request, pdb_code):
    try:
        structure = Structure.objects.get(pdb_code=pdb_code)
        chains = Chain.objects.filter(structure=structure)
        structuredomains = StructureDomain.objects.filter(chain__structure=structure)

        protein = structuredomains[0].domain.isoform.protein
        domains=[]
        for i in structuredomains:
            if i.domain not in domains:
                domains.append(i.domain)

        proteinsegments = ProteinSegment.objects.all()
        residuegenericnumbers = ResidueGenericNumber.objects.all()
        residues = Residue.objects.filter(domain__in=domains)
        
    except Structure.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'structure.html', {'structure' : structure, 'chains': chains, 'structuredomains' : structuredomains, 
                                            'protein': protein, 'domains': domains,
                                            'proteinsegments': proteinsegments, 'residuegenericnumbers': residuegenericnumbers, 'residues': residues})
    
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
