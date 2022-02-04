from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pdb_code>/', views.structure, name='structure'),
    path('<str:pdb_code>/<str:chain_ID>', views.chain, name='chain'),
    path('<str:pdb_code>/<str:chain_ID>/<str:domain>', views.domain, name='domain'),
]
