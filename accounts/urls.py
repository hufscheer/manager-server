from django.urls import path, include
from .views.login_views import CustomTokenObtainPairView
from .views.permission_test_view import PermissionTestView, MakePasswordTest

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('permission/', PermissionTestView.as_view(), name='PermissionTestView'),
    path('makepassword/', MakePasswordTest.as_view(), name='MakePasswordTest'),
]