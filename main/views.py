from django.shortcuts import render
from sectors.models import Sectors
def index(request):
    SectorsList = Sectors.objects.all()
    return render(request,'main/layout.html',{'Sectors': SectorsList})
