from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('algorithms', views.algorithms, name='algorithms'),
    path('results', views.results, name='results'),
]