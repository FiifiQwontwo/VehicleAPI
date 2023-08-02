from django.urls import path
from .views import BodyTypeList, BodyCreateAPI

urlpatterns = [
    path('list/', BodyTypeList.as_view(), name='list_bodyType'),
    path('new/', BodyCreateAPI.as_view(), name='new_bodyType'),

]
