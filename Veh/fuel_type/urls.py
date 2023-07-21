from django.urls import path
from .views import *


app_name = 'fuel_type'

urlpatterns = [
    path('list/', Fuellist.as_view(), name='list_cars_endpoint'),
    path('create/', CreateFuel.as_view(), name='new_car_endpoint'),


]
