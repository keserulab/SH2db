from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is SH2db protein page.")

def structure(request, pdb_code):
    return HttpResponse("Hello, world. This is the protein page for %s." % pdb_code)
    
def chain(request, pdb_code, chain_ID):
    return HttpResponse("Hello, world. This is the protein page for %s, %s." % (pdb_code, chain_ID) )
    
def domain(request, pdb_code, chain_ID, domain):
    return HttpResponse("Hello, world. This is the protein page for %s, %s, %s." % (pdb_code, chain_ID, domain) )