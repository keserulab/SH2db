from django.shortcuts import render

from django.http import HttpResponse

from protein.models import Protein, Domain


def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def browse(request):

    headers = ["Family", "Gene name", "Species", "Uniprot"]
    
    data = Protein.objects.all()
    
    return render(request, 'browse.html', {'data' : data, 'headers' : headers})

def charts(request):
    return render(request, 'charts.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

