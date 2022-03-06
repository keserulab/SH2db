from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pdb_code>_<str:domain>_<str:chain_ID>', views.structuredomain, name='structuredomain'),
    path('<str:pdb_code>_<str:chain_ID>', views.chain, name='chain'),
    path('<str:pdb_code>/', views.structure, name='structure'),   
]
