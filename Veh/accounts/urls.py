from django.urls import path
from .views import RegistrationView, LoginView, LogoutView, UserList
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_endpoint'),
    path('login/', LoginView.as_view(), name='login_endpoint'),
    path('logout/', LogoutView.as_view(), name='logout_endpoint'),
    path('users/', UserList.as_view(), name='userlist_endpoint'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
