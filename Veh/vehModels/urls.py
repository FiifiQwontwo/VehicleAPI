from django.urls import path
from .views import ListModels

urlpatterns = [
    path('all/', ListModels.as_view(), name='models_endpoint'),

]
