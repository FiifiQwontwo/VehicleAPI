from django.urls import path
from .views import ListModels

urlpatterns = [
    path('models/', ListModels.as_view(), name='models_endpoint'),

]
