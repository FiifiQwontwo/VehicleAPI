from django.urls import path
from .views import VehicleList, CreateVehicle, MakeDetailsAPI, UpdateVehicleMake


app_name = 'carMake'

urlpatterns = [
    path('list/', VehicleList.as_view(), name='list_cars_endpoint'),
    path('create/', CreateVehicle.as_view(), name='new_car_endpoint'),
    path('list/<int:pk>', MakeDetailsAPI.as_view(), name='details_endpoint'),
    path('update/<int:pk>', UpdateVehicleMake.as_view(), name='update_endpoint'),


]
