from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializer import ListVehicleSerializers, VehicleMakeDetailsSerializer, UpdateVehicleSerializer, \
    CreateVehicleSerializers
from .models import VehicleMake
from rest_framework.generics import UpdateAPIView
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class VehicleList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="List all Vehicles",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                        description='Manufacturer name (e.g., Toyota, '
                                                                    'Ford)'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),
                            'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                            'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                            'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),

                        },
                    ),

                ),

            ),
            400: 'Bad Request',
            401: "Unauthorized Request",
            403: "Forbidden",
            500: "Internal Server Error",
        }
    )
    def get(self, request):
        vehicle = VehicleMake.objects.all()
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarList(APIView):
    @swagger_auto_schema(
        operation_description="List all Cars",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                        description='Manufacturer name (e.g., Toyota, '
                                                                    'Ford)'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),
                            'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                            # 'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                            # 'is_motor': openapi.Schema(type=openapi.TYPE_STRING,  description='is motor'),

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
        vehicle = VehicleMake.objects.filter(is_car=True)
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MotorList(APIView):
    @swagger_auto_schema(
        operation_description="List all Motors",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING, description='Manufacturer name ('
                                                                                              'e.g., Toyota,'
                                                                                              'Ford)'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),
                            # 'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                            # 'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                            'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),

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
        vehicle = VehicleMake.objects.filter(is_motor=True)
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TractorList(APIView):
    @swagger_auto_schema(
        operation_description="List all Tractors",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                        description='Manufacturer name (e.g., Toyota, '
                                                                    'Ford)'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),
                            # 'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                            'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                            # 'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),

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
        vehicle = VehicleMake.objects.filter(is_tractor=True)
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MotorCarList(APIView):
    @swagger_auto_schema(
        operation_description="List Motor & Cars",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                        description='Manufacturer name (e.g., Toyota, '
                                                                    'Ford)'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),
                            'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                            # 'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                            'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),

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
        vehicle = VehicleMake.objects.filter(Q(is_car=True) & Q(is_motor=True))
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TractorCarList(APIView):
    @swagger_auto_schema(
        operation_description="List Tractor & Cars",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'make_name': openapi.Schema(type=openapi.TYPE_STRING,
                                                        description='Manufacturer name (e.g., Toyota, '
                                                                    'Ford)'),
                            'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                   description='logo'),
                            'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                            'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                            # 'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),

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
        vehicle = VehicleMake.objects.filter(Q(is_car=True) & Q(is_tractor=True))
        serializer = ListVehicleSerializers(vehicle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateVehicle(APIView):

    @swagger_auto_schema(
        operation_description="New Vehicle",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['make_name', 'logo', 'is_car', 'is_tractor', 'is_motor'],
            properties={
                'make_name': openapi.Schema(type=openapi.TYPE_STRING, description='Manufacturer name (e.g., Toyota, '
                                                                                  'Ford)'),
                'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
                'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),

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


class UpdateVehicleMake(UpdateAPIView):
    queryset = VehicleMake.objects.all()
    serializer_class = UpdateVehicleSerializer

    @swagger_auto_schema(
        operation_description="Update an existing Vehicle make",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['make_name', 'logo', 'is_car', 'is_tractor', 'is_motor'],
            properties={
                'make_name': openapi.Schema(type=openapi.TYPE_STRING, description='Manufacturer name (e.g., Toyota, '
                                                                                  'Ford)'),
                'status': openapi.Schema(type=openapi.TYPE_STRING),
                'logo': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
                'is_car': openapi.Schema(type=openapi.TYPE_STRING, description='is car'),
                'is_tractor': openapi.Schema(type=openapi.TYPE_STRING, description='is tractor'),
                'is_motor': openapi.Schema(type=openapi.TYPE_STRING, description='is motor'),
            }
        ),
        responses={
            200: 'Vehicle Make  updated successfully',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Vehicle Make not found',
            500: 'Internal Server Error',
        }
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class MakeDetailsAPI(APIView):
    @swagger_auto_schema(
        operation_description="Vehicle Make Details",
        response={
            200: VehicleMakeDetailsSerializer(),
            404: "Vehicle not found",
        }
    )
    def get(self, request, pk):
        try:
            make = VehicleMake.objects.get(pk=pk)
            serializer = VehicleMakeDetailsSerializer(make)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except VehicleMake.DoesNotExist:
            return Response({'Error': 'Vehicle Make not found'}, status=status.HTTP_404_NOT_FOUND)


class VehicleMakeDelete(APIView):
    @swagger_auto_schema(
        operation_description="Delete a vehicle Make",
        responses={
            204: "Vehicle Make Deleted",
            404: "Vehicle Make Not Found",
        }
    )
    def delete(self, request, pk):
        try:
            make = VehicleMake.objects.get(pk=pk)
            make.delete()
            return Response({'Message': "Vehicle deleted"}, status=status.HTTP_204_NO_CONTENT)
        except VehicleMake.DoesNotExist:
            return Response({'Error': "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
