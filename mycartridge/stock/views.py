from django.http import HttpResponse
from .models import Data
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView


class DataListView(ListView):
    model = Data
    template_name = 'stock/index.html'

