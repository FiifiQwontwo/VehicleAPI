from django.shortcuts import render
from .models import VehicleModel
from .serializer import ModelListSerializer, ModelDetailsSerializer, ModelCreateSerializer, ModelUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



# Create your views here.

class ListModels(APIView):
    @swagger_auto_schema(
        operation_description="List all Models",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make': openapi.Schema(type=openapi.TYPE_STRING, description='Manufacturer name ('
                                                                                         'e.g., Toyota,'
                                                                                         'Ford)'),
                            'model_name': openapi.Schema(type=openapi.TYPE_STRING, description='Model name ('
                                                                                               'e.g., DBX,'
                                                                                               'Corolla)'),
                            'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                      description='picture'),

                        },
                    ),

                ),

            ),
            400: 'Bad Request',
            401: "Unautorized Request",
            403: "Forbidden",
            500: "Internal Server Error",
        }
    )
    def get(self, request):
        asd = VehicleModel.objects.all()
        serializer = ModelListSerializer(asd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateModel(APIView):
    @swagger_auto_schema(
        operation_description="New Model",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['make', 'model_naame', 'picture'],
            properties={
                'make': openapi.Schema(type=openapi.TYPE_STRING, description='New Model'),
                'model_name': openapi.Schema(type=openapi.TYPE_STRING, description='Model Name'),
                'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
            }
        ),
        responses={
            201: 'Created Model',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }

    )
    def post(self, request):
        serializer = ModelCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsModels(APIView):
    @swagger_auto_schema(
        operation_description="Details models",
        response={
            200: ModelDetailsSerializer(),

        }
    )
    def get(self, request, pk):
        try:
            details = VehicleModel.objects.get(pk=pk)
            serializer = ModelDetailsSerializer(details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except VehicleModel.DoesNotExist:
            return Response({'Error': 'Vehicle model does not exist'}, status=status.HTTP_404_NOT_FOUND)
