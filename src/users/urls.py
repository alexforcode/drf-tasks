from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.api import views


app_name = 'users'

urlpatterns = [
    path('me/', views.SelfView.as_view(), name='self'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]
