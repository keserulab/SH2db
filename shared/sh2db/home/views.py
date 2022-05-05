from django.shortcuts import render

from django.http import HttpResponse

from protein.models import Protein, Domain, ProteinSegment
from residue.models import Residue, ResidueGenericNumber
from common.alignment import Alignment
from django.db.models import Count

from structure.models import Structure, StructureDomain

import csv

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


def get_csv(request, x, y):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

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

            headerline.append('proteins')
            writer.writerow(headerline)
            for row in counts:
                writer.writerow([row, counts[row]])

            return response

        else:
            lookup_string = {'family': 'family__name',
                            'species': 'species__latin_name'}[x]
            lookup = Protein.objects.all().values(lookup_string).annotate(count_items=Count('id'))
            
        headerline.append('proteins')
    elif y=='structure':
        if x=='year':
            lookup_string = {'year': 'publication__year'}[x]
            lookup = Structure.objects.all().values(lookup_string).annotate(count_items=Count('id'))
        else:
            lookup_string = {'family': 'domain__parent__isoform__protein__family__name',
                            'species': 'domain__parent__isoform__protein__species__latin_name'}[x]
            groupby_string = 'chain__structure__id'
            lookup = StructureDomain.objects.all().values(lookup_string).annotate(count_items=Count(groupby_string))

        headerline.append('structures')
    elif y=='structuredomain':
        lookup_string = {'family': 'domain__parent__isoform__protein__family__name',
                                'year': 'chain__structure__publication__year',
                                'species': 'domain__parent__isoform__protein__species__latin_name'}[x]
        lookup = StructureDomain.objects.all().values(lookup_string).annotate(count_items=Count('id'))

        headerline.append('structuredomains')
    elif y=='publication':
        pass

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

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

