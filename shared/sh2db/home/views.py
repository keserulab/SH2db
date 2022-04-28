from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

from django.db.models import Count

from protein.models import Protein

from structure.models import StructureDomain

import pandas as pd

import csv

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def browse(request):

    headers = ["Family", "Gene name", "Species", "Uniprot"]
    
    data = Protein.objects.all()
    
    return render(request, 'browse.html', {'data' : data, 'headers' : headers})


def get_csv(request, search_string):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)


    search_string_proteins = {'family': 'family__name',
                                'species': 'species__latin_name'
    }
    search_string_structures = {'family': 'domain__parent__isoform__protein__family__name',
                                'year': 'chain__structure__publication__year',
                                'species': 'domain__parent__isoform__protein__species__latin_name'
    }
    
    headerline=['group']
    
    try:
        proteins = Protein.objects.all().values(search_string_proteins[search_string]).annotate(count_items=Count('id'))
        headerline.append('proteins')
    except KeyError:
        pass
    try:
        structures = StructureDomain.objects.all().values(search_string_structures[search_string]).annotate(count_items=Count('id'))
        headerline.append('structures')
    except KeyError:
        pass  

    writer.writerow(headerline)

    if proteins and structures:
        for row in zip(proteins,structures):
            lista = list(row[0].values())
            lista.append(list(row[1].values())[1])
            writer.writerow(lista)
    elif structures:
        for row in structures:
            lista = row.values()
            writer.writerow(row.values())
    elif proteins:
        for row in proteins:
            lista = row.values()
            writer.writerow(lista)
    

    return response

def charts(request):
    search_string = 'species'

    return render(request, 'charts.html', {'search_string' : search_string})

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

