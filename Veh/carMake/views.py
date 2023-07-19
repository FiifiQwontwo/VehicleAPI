from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializer import ListVehicleSerializers, CreateVehicleSerializers
from .models import VehicleMake

# Create your views here.


class VehicleList(APIView):
    @swagger_auto_schema(
        operation_description="List vehicle",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING, description='name of vehicle'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),

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
        vehicle = VehicleMake.objects.all()
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateVehicle(APIView):

    @swagger_auto_schema(
        operation_description="New Vehicle",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['make_name', 'logo'],
            properties={
                'make_name': openapi.Schema(type=openapi.TYPE_STRING),
                'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),

            }
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',

        }
    )
    def post(self, request):
        serializer = CreateVehicleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
