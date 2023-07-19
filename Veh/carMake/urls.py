from django.urls import path
from .views import VehicleList, CreateVehicle


app_name = 'carMake'

urlpatterns = [
    path('list/', VehicleList.as_view(), name='list_cars_endpoint'),
    path('create/', CreateVehicle.as_view(), name='new_car_endpoint'),


]
