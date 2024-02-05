from django.urls import path
from .views import VehicleList, CreateVehicle, MakeDetailsAPI, UpdateVehicleMake, CarList, MotorList, TractorList, \
    MotorCarList, TractorCarList, VehicleMakeDelete


app_name = 'carMake'

urlpatterns = [
    path('vehicles/', VehicleList.as_view(), name='vehicles_list_endpoint'),
    path('cars/', CarList.as_view(), name='list_cars_endpoint'),
    path('motors/', MotorList.as_view(), name='list_motor_endpoint'),
    path('tractors/', TractorList.as_view(), name='list_tractors_endpoint'),
    path('carsandmotors/', MotorCarList.as_view(), name='list_cars&motors_endpoint'),
    path('carsandtractors/', TractorCarList.as_view(), name='list_cars&tractors_endpoint'),
    path('vehicles/create/', CreateVehicle.as_view(), name='new_car_endpoint'),
    path('vehicles/<int:pk>', MakeDetailsAPI.as_view(), name='details_endpoint'),
    path('vehicles/<int:pk>', VehicleMakeDelete.as_view(), name='delete_endpoint'),
    path('vehicles/update/<int:pk>', UpdateVehicleMake.as_view(), name='update_endpoint'),


]
