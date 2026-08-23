from django.urls import path 
from .views import SectorInfo, SectorList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',SectorList.as_view(),name = 'sectorlist'),
    path('sector/<slug:slug>/',SectorInfo.as_view(),name = 'sectorinfo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
