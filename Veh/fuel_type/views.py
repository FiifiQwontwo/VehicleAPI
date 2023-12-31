from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializer import ListFuelSerializer, UpdateFuelSerializer, CreateFuelSerializer
from .models import Fuel
from rest_framework.generics import UpdateAPIView


# Create your views here.
class ListFuelView(APIView):

    @swagger_auto_schema(
        operation_description='List Fuel',
        responses={
            200: openapi.Response(
                description='OK',
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'Fuel_Type': openapi.Schema(type=openapi.TYPE_STRING, description='name of Fuel'),
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
        fuel = Fuel.objects.all()
        serializer = ListFuelSerializer(fuel, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FuelDetails(APIView):

    @swagger_auto_schema(
        operation_description="Fuel details",
        responses={
            200: ListFuelSerializer(),
            404: "Fuel details not found",
        }
    )
    def get(self, request, pk):
        try:
            fuel = Fuel.objects.get(pk=pk)
            serializer = ListFuelSerializer(fuel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Fuel.DoesNotExist:
            return Response({"Error": "Fuel Type not Found"}, status=status.HTTP_404_NOT_FOUND)


# continue to work with it
class CreateFuelAPI(APIView):

    @swagger_auto_schema(
        operation_description="New Fuel",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['fuel_type'],
            properties={
                'fuel_type': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: "Created",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            500: "Internal Server Error",
        }

    )
    def post(self, request):
        serializer = CreateFuelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)


class UpdateFuelAPI(UpdateAPIView):
    queryset = Fuel.objects.all()
    serializer_class = UpdateFuelSerializer

    @swagger_auto_schema(
        operation_description="Update an existing Fuel Type ",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['fuel_type'],
            properties={
                'fuel_type': openapi.Schema(type=openapi.TYPE_STRING, description='fuel type'),
            }

        ),
        responses={
            200: 'Fuel_type  updated successfully',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Fuel_type not found',
            500: 'Internal Server Error',
        }
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteFuelType(APIView):

    @swagger_auto_schema(
        operation_description="Delete Fuel Type",
        responses={
            204: "Fuel Type Deleted",
            404: "Fuel Type Not Found",
        }
    )
    def delete(self, request, pk):
        try:
            fuel = Fuel.objects.get(pk=pk)
            fuel.delete()
            return Response({'Message': "Fuel Type Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Fuel.DoesNotExist:
            return Response({Error: "Fuel Type Deleted"}, status=status.HTTP_204_NO_CONTENT)
