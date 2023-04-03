from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from django.views.generic import View


from structure.models import Structure, Chain, StructureDomain
from residue.models import Residue, ResidueGenericNumber
from protein.models import ProteinSegment, Domain
from common.alignment import Alignment

from io import StringIO, BytesIO
from Bio.PDB import PDBIO, PDBParser
import zipfile

from datetime import datetime

import subprocess
from random import randint
import os

def pymoldownload(request):
    [os.remove(i) for i in os.listdir() if i.startswith('SH2db_pymol_session')]
    structures = request.GET['ids'].split(',')

    domains = Domain.objects.filter(name__in=structures)

    structure_domains = [i.structure_domain.all() for i in domains]#structure_domains + af_domains
    residues = request.GET['residues']

    pdbnames=[]
    for structure_domain in structure_domains:
        if not structure_domain[0].domain.parent:
            pdbname = structure_domain[0].domain.isoform.protein.accession+'-AF-'+structure_domain[0].domain.domain_type.slug+'.pdb'
        else:
            pdbname = structure_domain[0].domain.name+'.pdb'
        with open(pdbname, 'w') as f:
            f.write(structure_domain[0].pdbdata.pdb)
        pdbnames.append(pdbname)

    ## FOR DEBUGGING
    io = BytesIO()

    ## GENERATE PYMOL SESSION
    outfilename = 'SH2db_pymol_session'+str(randint(0,10000000))+'.pse'
    result = subprocess.run(["python2.7", os.getcwd()+"/structure/pymol_session_new.py", outfilename, 
                                str([ pdbname for pdbname in pdbnames]), str(residues)], capture_output=True)

    for pdbname in pdbnames:
        os.remove(pdbname)

    ## FOR DEBUGGING
    io.write(result.stdout)

    response = FileResponse( open(outfilename, "rb"), as_attachment=True)#, filename=outfilename) 

    ## FOR DEBUGGING
    #response = HttpResponse(io.getvalue(), content_type='application/x-zip-compressed')
    #response['Content-Disposition'] = 'attachment; filename=%s' % outfilename
    #response['Content-Length'] = io.tell()
    return response

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
            if structure[0].chain.structure.pdb_code:
                file_name = '{}_{}.pdb'.format(structure[0].domain.isoform.protein.name, structure[0].domain.name)
            else:
                file_name = '{}_{}_AF_{}.pdb'.format(structure[0].domain.isoform.protein.name, structure[0].domain.isoform.protein.accession, structure[0].domain.domain_type.slug)
            backup_zip.writestr(file_name, io.getvalue())


    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")


    response = HttpResponse(zip_io.getvalue(), content_type='application/x-zip-compressed')
    response['Content-Disposition'] = 'attachment; filename=%s' % 'SH2DB_structures' + dt_string + ".zip"
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
        alphafold = False
        if pdb_code.endswith('-AF'):
            structure = Structure.objects.get(protein__accession=pdb_code.split('-')[0], pdb_code__isnull=True)
            alphafold = True
        else:
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
            if alphafold:
                domains = [i.domain for i in structuredomains]
            else:
                domains = list(parent_domains) + [i.domain for i in structuredomains]
        else:
            if alphafold:
                domains = [i.domain for i in structuredomains if i.domain.domain_type.slug=='N'] + [i.domain for i in structuredomains if i.domain.domain_type.slug=='C']
            else:
                domains = [parent_domains[0]] + [i.domain for i in structuredomains if i.domain.domain_type.slug=='N'] + [parent_domains[1]] + [i.domain for i in structuredomains if i.domain.domain_type.slug=='C']

        alignment = Alignment(domains)
        segments, gns, residues, sheinerman = alignment.align_domain_residues()

        segmentlist=[]
        for segment,colnum in segments.items():
            for i in range(colnum):
                segmentlist.append(segment.slug)
        gnzips = [x+y for x,y in zip(segmentlist,gns)]
            
    except Structure.DoesNotExist:
        return render(request, 'error.html')

    return render(request, 'structure.html', {'structure' : structure, 'chains': chains, 'structuredomains' : structuredomains, 
                                            'protein': protein, 'domains': domains,
                                            'proteinsegments': proteinsegments, 'residuegenericnumbers': residuegenericnumbers, 'residues': residues,
                                            'gns': gns, 'segments': segments, 'parent_domains': parent_domains, 'checkbox': True,
                                            'gnzips': gnzips, 'alphafold': alphafold, 'sheinerman': sheinerman})
    

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
