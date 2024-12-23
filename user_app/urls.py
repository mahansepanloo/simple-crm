from django.urls import path
from user_app.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView



urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('logout/', TokenBlacklistView.as_view(), name='blacklist'),

]