from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is SH2db protein page.")

def protein(request, name):
    return HttpResponse("Hello, world. This is the protein page for %s." % name)