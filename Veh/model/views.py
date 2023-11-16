from django.shortcuts import render
from .models import VehicleModel
from .serailizer import ModelListSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class ListModels(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes =[IsAuthenticated]

    @swagger_auto_schema(
        operation_description = "List models",

    )

    def get(self, request):
        asd = VehicleModel.objects.all()
        serializer = ModelListSerializer(asd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
