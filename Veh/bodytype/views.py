from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import BodyType
from .serializer import ListBodySerializer, CreateBodyType


# Create your views here.
class BodyTypeList(APIView):
    @swagger_auto_schema(
        operation_description="List all Body Types",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'body_type': openapi.Schema(type=openapi.TYPE_STRING, description='body_type_name'),
                            'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                      description='picture'),
                            'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
                        },
                    ),
                ),

            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        body = BodyType.objects.all()
        serializer = ListBodySerializer(body, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BodyCreateAPI(APIView):

    @swagger_auto_schema(
        operation_description='Create a new Body Type',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['body_type', 'picture', 'description'],
            properties={
                "body_type": openapi.Schema(type=openapi.TYPE_STRING, description='Body Type Name'),
                "picture": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                          description='Picture of Body Type'),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description='Description of Body Type'),
            }
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal ServerError'
        }
    )
    def post(self, request):
        serializer = CreateBodyType(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
