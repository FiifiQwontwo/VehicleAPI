from django.urls import path
from .views import BodyTypeList

urlpatterns = [
    path('list/', BodyTypeList.as_view(), name='list_bodyType'),

]
