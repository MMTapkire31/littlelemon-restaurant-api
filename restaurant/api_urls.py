from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import BookingViewSet, MenuItemViewSet, RegistrationView

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("booking", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
]
