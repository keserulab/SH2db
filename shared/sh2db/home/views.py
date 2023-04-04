from django.shortcuts import render

from django.http import HttpResponse, FileResponse

from protein.models import Protein, Domain, ProteinSegment
from residue.models import Residue, ResidueGenericNumber
from common.models import Publication
from common.alignment import Alignment
from django.db.models import Count

from structure.models import Structure, StructureDomain

from io import StringIO, BytesIO
import zipfile

import subprocess
from random import randint
import os
import csv

def index(request):
    return render(request, 'index.html')

def search(request):
    domains = Domain.objects.all().order_by('isoform__protein__name', 'domain_type', '-parent', 'name')

    proteinsegments = ProteinSegment.objects.all()
    residuegenericnumbers = ResidueGenericNumber.objects.all()
    residues = Residue.objects.filter(domain__in=domains).prefetch_related('domain', 'protein_segment', 'generic_number')

    alignment = Alignment(domains)
    segments, gns, residues, sheinerman = alignment.align_domain_residues()

    return render(request, 'search.html', { 'domains': domains,
                                            'proteinsegments': proteinsegments, 'residuegenericnumbers': residuegenericnumbers, 'residues': residues,
                                            'gns': gns, 'segments': segments, 'checkbox': True, 'filter': True, 'alphafold': True, 'sheinerman': sheinerman})
    

def browse(request):

    headers = ["Family", "Gene name", "Species", "Uniprot"]
    
    data = Protein.objects.all()
    
    return render(request, 'browse.html', {'data' : data, 'headers' : headers})


def get_csv(request, x, y):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
    #    headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    response['Content-Disposition']='attachment; filename="somefilename.csv"'

    writer = csv.writer(response)

    headerline=['group']
    if y=='protein':
        if x=='no_sh2':
            lookup_string = {'no_sh2': 'isoform__protein'}[x]
            lookup = Domain.objects.filter(parent__id__isnull=True).values(lookup_string).annotate(count_items=Count('id'))

            counts={}
            for row in lookup:
                try:
                    counts[list(row.values())[1]] += 1
                except KeyError:
                    counts[list(row.values())[1]] = 1

            # Sort dictionary by keys
            counts2={}
            for i in sorted(counts):
                counts2[i]=counts[i]
            counts=counts2

            headerline.append('count')
            writer.writerow(headerline)
            for row in counts:
                writer.writerow([row, counts[row]])

            return response

        else:
            lookup_string = {'family': 'family__name',
                            'species': 'species__latin_name'}[x]
            lookup = Protein.objects.all().values(lookup_string).order_by(lookup_string).annotate(count_items=Count('id'))
            
        headerline.append('count')
    elif y=='structure':
        if x=='no_sh2':
            lookup_string = {'no_sh2': 'chain__structure'}[x]
            lookup = StructureDomain.objects.filter(chain__structure__pdb_code__isnull=False).values(lookup_string).annotate(count_items=Count('id'))

            counts={}
            for row in lookup:
                try:
                    counts[list(row.values())[1]] += 1
                except KeyError:
                    counts[list(row.values())[1]] = 1

            # Sort dictionary by keys
            counts2={}
            for i in sorted(counts):
                counts2[i]=counts[i]
            counts=counts2

            headerline.append('count')
            writer.writerow(headerline)
            for row in counts:
                writer.writerow([row, counts[row]])

            return response

        else:
            lookup_string = {'year': 'publication__year',
                            'family': 'protein__family__name',
                            'species': 'protein__species__latin_name'}[x]

            lookup = Structure.objects.filter(pdb_code__isnull=False, publication__isnull=False).values(lookup_string).order_by(lookup_string).annotate(count_items=Count('id'))

        headerline.append('count')
    elif y=='structuredomain':
        lookup_string = {'family': 'domain__parent__isoform__protein__family__name',
                                'year': 'chain__structure__publication__year',
                                'species': 'domain__parent__isoform__protein__species__latin_name'}[x]
        lookup = StructureDomain.objects.filter(chain__structure__pdb_code__isnull=False).values(lookup_string).order_by(lookup_string).annotate(count_items=Count('id'))

        headerline.append('count')
    elif y=='publication':
        if x=='no_sh2':
            lookup_string = {'no_sh2': 'chain__structure__publication'}[x]
            lookup = StructureDomain.objects.filter(chain__structure__pdb_code__isnull=False).values(lookup_string).annotate(count_items=Count('id'))

            counts={}
            for row in lookup:
                try:
                    counts[list(row.values())[1]] += 1
                except KeyError:
                    counts[list(row.values())[1]] = 1

            # Sort dictionary by keys
            counts2={}
            for i in sorted(counts):
                counts2[i]=counts[i]
            counts=counts2

            headerline.append('count')
            writer.writerow(headerline)
            for row in counts:
                writer.writerow([row, counts[row]])

            return response

        elif x=='family' or x=='species': # NOT WORKING YET!!
            lookup_string = {'family': 'protein__family__name',
                            'species': 'protein__species__latin_name'}[x]
            #lookup = Structure.objects.all().values(lookup_string).annotate(count_items=Count('id'))
            headerline.append('count')

        else:
            lookup_string = {'year': 'year'}[x]
            lookup = Publication.objects.all().values(lookup_string).order_by(lookup_string).annotate(count_items=Count('id'))
            headerline.append('count')

    writer.writerow(headerline)
    for row in lookup:
        writer.writerow(row.values())

    #if proteins and structures:
    #    for row in zip(proteins,structures):
    #        lista = list(row[0].values())
    #        lista.append(list(row[1].values())[1])
    #        writer.writerow(lista)
    return response

def charts(request):
    return render(request, 'charts.html')

def about(request):
    return render(request, 'about.html')

def documentation(request):
    return render(request, 'documentation.html')