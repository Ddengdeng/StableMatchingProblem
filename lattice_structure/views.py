from django.shortcuts import render
from django.http import HttpResponse
# from SearchSM import SearchSM


def index(request):

    return render(request, 'lattice_structure/index.html')

