from django.urls import path
from . import views

urlpatterns = [
    path('bus-timing/', views.bus_timings, name='bus_timing'),
]