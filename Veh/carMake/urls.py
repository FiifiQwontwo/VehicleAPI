from django.urls import path
from .views import VehicleList, CreateVehicle, MakeDetailsAPI, UpdateVehicleMake, CarList, MotorList, TractorList, \
    MotorCarList, TractorCarList, VehicleMakeDelete


app_name = 'carMake'

urlpatterns = [
    path('vehicleslist/', VehicleList.as_view(), name='vehicles_list_endpoint'),
    path('allcars/', CarList.as_view(), name='list_cars_endpoint'),
    path('allmotors/', MotorList.as_view(), name='list_motor_endpoint'),
    path('alltractors/', TractorList.as_view(), name='list_tractors_endpoint'),
    path('carsandmotor/', MotorCarList.as_view(), name='list_cars&motors_endpoint'),
    path('carsandtractor/', TractorCarList.as_view(), name='list_cars&tractors_endpoint'),
    path('create/', CreateVehicle.as_view(), name='new_car_endpoint'),
    path('vehicleslist/<int:pk>', MakeDetailsAPI.as_view(), name='details_endpoint'),
    path('list/<int:pk>', VehicleMakeDelete.as_view(), name='details_endpoint'),
    path('update/<int:pk>', UpdateVehicleMake.as_view(), name='update_endpoint'),


]
