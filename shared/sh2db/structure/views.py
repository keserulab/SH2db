from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import View


from structure.models import Structure, Chain, StructureDomain
from residue.models import Residue, ResidueGenericNumber
from protein.models import ProteinSegment, Domain
from common.alignment import Alignment

from io import StringIO, BytesIO
from Bio.PDB import PDBIO, PDBParser
import zipfile


def structuredownload(request):
    # if request.is_ajax and request.method == 'GET':
    # structures = request.GET.get("structures", None)
    structures = request.GET['ids'].split(',')
    domains = Domain.objects.filter(name__in=structures)
    structure_domains = [i.structure_domain.all() for i in domains]

    zip_io = BytesIO()
    with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_DEFLATED) as backup_zip:
        for structure in structure_domains:
            io = StringIO(structure[0].pdbdata.pdb)        
            file_name = '{}_{}.pdb'.format(structure[0].domain.isoform.protein.name, structure[0].domain.name)
            backup_zip.writestr(file_name, io.getvalue())

    response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'SH2DB_structures' + ".zip"
    response['Content-Length'] = zip_io.tell()
    return response


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

        parent_domains = Domain.objects.filter(isoform__protein=protein, parent__isnull=True).order_by('-domain_type__slug')
        if len(parent_domains)==1:
            domains = list(parent_domains) + [i.domain for i in structuredomains]
        else:
            domains = [parent_domains[0]] + [i.domain for i in structuredomains if i.domain.domain_type.slug=='N'] + [parent_domains[1]] + [i.domain for i in structuredomains if i.domain.domain_type.slug=='C']

        alignment = Alignment(domains)
        segments, gns, residues = alignment.align_domain_residues()
        
    except Structure.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'structure.html', {'structure' : structure, 'chains': chains, 'structuredomains' : structuredomains, 
                                            'protein': protein, 'domains': domains,
                                            'proteinsegments': proteinsegments, 'residuegenericnumbers': residuegenericnumbers, 'residues': residues,
                                            'gns': gns, 'segments': segments, 'parent_domains': parent_domains, 'checkbox': True})
    
def pymol_session(request, structuredomains, residues):
    return "asdasd"

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
