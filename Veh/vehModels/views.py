from django.shortcuts import render
from .models import VehicleModel
from .serializer import ModelListSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class ListModels(APIView):
    def get(self, request):
        asd = VehicleModel.objects.all()
        serializer = ModelListSerializer(asd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
