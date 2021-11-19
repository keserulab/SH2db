from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'templates/search.html')

def browse(request):
    return render(request, 'templates/browse.html')

def charts(request):
    return render(request, 'templates/charts.html')

def faq(request):
    return render(request, 'templates/faq.html')

def contact(request):
    return render(request, 'templates/contact.html')

