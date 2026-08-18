from django.urls import path 
from . import views
urlpatterns = [
    path('',views.index),
    path('<int:pk>/',views.Dinamic.as_view(),name = 'Sector_view')
]

