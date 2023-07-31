from django.urls import path
from .views import (ListFuelView, FuelDetails, CreateFuelAPI, DeleteFuelType,
                    UpdateFuelAPI)

app_name = 'fuel_type'

urlpatterns = [
    path('all/', ListFuelView.as_view(), name='list_fueltype_endpoint'),
    path('all/<int:pk>', FuelDetails.as_view(), name='fuel_details_endpoint'),
    path('create/', CreateFuelAPI.as_view(), name='create_fuel_api_endpoint'),
    path('delete/<int:pk>', DeleteFuelType.as_view(), name='delete_endpoint'),
    path('update/<int:pk>', UpdateFuelAPI.as_view(), name='update_fuel_api_endpoint'),

]
