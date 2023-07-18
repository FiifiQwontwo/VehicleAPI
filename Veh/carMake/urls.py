from django.urls import path
from .views import VehicleList


app_name = 'carMake'

urlpatterns = [
    path('list/', VehicleList.as_view(), name='list_cars_endpoint'),


]
