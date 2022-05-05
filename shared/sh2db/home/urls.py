from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('search', cache_page(60*60*24*30)(views.search), name='search'),
    path('browse', views.browse, name='browse'),
    path('charts', views.charts, name='charts'),
    path('get_csv/<str:x>/<str:y>', views.get_csv, name='get_csv'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact')
]