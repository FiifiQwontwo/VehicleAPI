from django.urls import path
from .views import ListFuelView, FuelDetails

app_name = 'fuel_type'

urlpatterns = [
    path('all/', ListFuelView.as_view(), name='list_fueltype_endpoint'),
    path('list/<int:pk>', FuelDetails.as_view(), name='fuel_details_endpoint'),

]
