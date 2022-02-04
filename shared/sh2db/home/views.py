from django.shortcuts import render

from django.http import HttpResponse

import pandas as pd
import json

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def browse(request):
    df = pd.read_csv("home/static/data/protein_data.csv")
    
    headers = df.columns
    
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    
    return render(request, 'browse.html', {'data' : data, 'headers' : headers})

def charts(request):
    return render(request, 'charts.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

