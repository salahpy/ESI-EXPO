from django.contrib import admin
from django.urls import include, path
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#middleware check if he is authencation

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("login/", TokenCreateView.as_view(), name="token_create"),
    path("logout/", TokenDestroyView.as_view(), name="token_destroy"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
