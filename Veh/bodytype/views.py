from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import BodyType
from .serializer import ListBodySerializer, CreateBodyType, UpdateBodyTypeSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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



@permission_classes([IsAuthenticated, IsAdminUser])
class BodyCreateAPI(APIView):

    @swagger_auto_schema(
        operation_description="New Body Type",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['body_type', 'picture', 'description'],
            properties={
                'body_type': openapi.Schema(type=openapi.TYPE_STRING),
                'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),

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
        serializer = CreateBodyType(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated, IsAdminUser])
class UpdateBodyTypeAPI(UpdateAPIView):
    queryset = BodyType.objects.all()
    serializer_class = UpdateBodyTypeSerializer

    @swagger_auto_schema(
        operation_description="Update body type",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['body_type', 'picture', 'description'],
            properties={
                'body_type': openapi.Schema(type=openapi.TYPE_STRING, description='body type name'),
                'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
            }
        ),
        responses={
            200: 'Body Type Updated',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found',
            500: 'Internal Server Error',
        }
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class BodyTypeDetails(APIView):

    @swagger_auto_schema(
        operation_description="Body Type Details",
        response={
            200: ListBodySerializer(),
            404: 'Body Type Not Found',
        }
    )
    def get(self, request, pk):
        try:
            body = BodyType.objects.get(pk=pk)
            serializer = ListBodySerializer(body)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BodyType.DoesNotExist:
            return Response({'Error': 'Body_type not found'}, status=status.HTTP_404_NOT_FOUND)


@permission_classes([IsAdminUser])
class BodyTypeDeleteAPI(APIView):
    @swagger_auto_schema(
        operation_description ="Delete a body type",
        response ={
            204: "Body Type deleted",
            404: "Body Type not found",
        }
    )
    def delete(self, request, pk):
        try:
            by =BodyType.objects.get(pk=pk)
            by.delete()
            return Response({'Messsage':'Body Type Deleted'}, status=status.HTTP_204_NO_CONTENT)
        except BodyType.DoesNotExist:
            return Response({'Error':"BodyType  not found"}, status=status.HTTP_404_NOT_FOUND)