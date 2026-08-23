from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ModelInfo 

class SectorList(ListView):
    model = ModelInfo
    template_name = 'main/layout.html'
    context_object_name = 'sectors'


class SectorInfo(DetailView):
    model = ModelInfo
    template_name = "main/sector.html"
    context_object_name = 'sector'
