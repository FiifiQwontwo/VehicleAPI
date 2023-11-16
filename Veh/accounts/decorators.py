from rest_framework.decorators import permission_classes, user_passes_test
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

def user_is_staff(user):
    return user.is_authenticated and user.is_staff

@permission_classes([IsAuthenticated, IsAdminUser])
def staff_required(request, *args, **kwargs):
    return Response({"message": "You have staff permissions."}, status=status.HTTP_200_OK)