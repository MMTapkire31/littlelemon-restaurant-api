from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer, RegistrationSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("id")
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
