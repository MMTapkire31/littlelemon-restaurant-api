from django.contrib import admin
from django.urls import include, path
from restaurant import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("book/", views.book, name="book"),
    path("reservations/", views.reservations, name="reservations"),
    path("bookings/", views.bookings_api, name="bookings_api"),
    path("restaurant/", include("restaurant.api_urls")),
]
