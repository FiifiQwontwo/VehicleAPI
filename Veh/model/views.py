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
        responses = {
            200:openapi.Response(
                description = "OK",
                schema = openapi.Schema(
                    type =openapi.TYPE_ARRAY,
                    items =openapi.Schema(
                        type =openapi.TYPE_OBJECT,
                        properties ={
                            'make': openapi.Schema(type =openapi.TYPE_STRING,description='Manufacturer name (e.g., Toyota, '
                                                                    'Ford)'),
                            'model_name': openapi.Schema(type =openapi.TYPE_STRING, description='Model name'),
                            'picture': openapi.Schema(type =openapi.TYPE_STRING, format =openapi.FORMAT_BINARY, description='Picture')

                        },
                    ),
                ),
            ),
            400:'Bad request',
            401: "Unauthorized Request",
            403: "Forbidden",
            500: "Internal Server Error",
        }

    )

    def get(self, request):
        asd = VehicleModel.objects.all()
        serializer = ModelListSerializer(asd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
