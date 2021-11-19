from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def browse(request):
    return render(request, 'browse.html')

def charts(request):
    return render(request, 'charts.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')

