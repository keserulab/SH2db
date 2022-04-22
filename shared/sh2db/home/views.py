from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

from django.db.models import Count

from protein.models import Protein

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


def get_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['group', 'Nitrogen', 'normal', 'stress'])
    writer.writerow(['banana', '12', '1', '13'])
    writer.writerow(['poacee', '6', '6', '33'])
    writer.writerow(['sorgho', '11', '28', '12'])
    writer.writerow(['triticum', '19', '6', '1'])

    df = pd.DataFrame(columns=['group', 'Nitrogen', 'normal', 'stress'])
    df.loc[0]=['banana', '12', '1', '13']
    df.loc[1]=['poacee', '6', '6', '33']
    df.loc[2]=['sorgho', '11', '28', '12']
    df.loc[3]=['triticum', '19', '6', '1']

    data = Protein.objects.all().values('family').annotate(count_items=Count('id'))

    return JsonResponse(df.to_json(), safe=False)

def charts(request):

    csv = get_csv(request)
    #csv = {'group': ['banana', 'poacee', 'sorgho', 'triticum'],'Nitrogen': [12,6,11,19],'normal': [1,6,28,6],'stress': [13,33,12,1]}
    
    return render(request, 'charts.html', {'csv' : csv})

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

