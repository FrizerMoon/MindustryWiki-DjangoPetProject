from django.shortcuts import render
from .models import Sectors
from django.views.generic import DetailView

def index(request):
    Sectors = Sectors.objects.all()
    return render(request,'main/sectors.html',{'Sectors': Sectors})

class Dinamic(DetailView):
    model = Sectors
    template_name = 'sectors/dinamic_sectors.html' 
    context_object_name = 'sectorss'
