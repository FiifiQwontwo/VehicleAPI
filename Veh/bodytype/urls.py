from django.urls import path
from .views import BodyTypeList, BodyCreateAPI, UpdateBodyTypeAPI, BodyTypeDeleteAPI, BodyTypeDetails

urlpatterns = [
    path('list/', BodyTypeList.as_view(), name='list_bodyType'),
    path('new/', BodyCreateAPI.as_view(), name='new_bodyType'),
    path('list/<int:pk>', BodyTypeDetails.as_view(), name='body type details'),
    path('update/<int:pk>', UpdateBodyTypeAPI.as_view(), name='update body type'),
    path('delete/<int:pk>', BodyTypeDeleteAPI.as_view(), name='update body type'),



]
