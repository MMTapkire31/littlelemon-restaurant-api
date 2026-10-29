import json
from datetime import date
from django.db import IntegrityError, transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from .models import Booking

SLOTS = [f"{hour:02d}:00" for hour in range(17, 23)]

def home(request):
    return render(request, "restaurant/home.html")

def book(request):
    today = date.today().isoformat()
    message = ""
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        reservation_date = request.POST.get("reservation_date", "").strip()
        reservation_slot = request.POST.get("reservation_slot", "").strip()
        if not first_name or not reservation_date or not reservation_slot:
            message = "Please complete all fields."
        else:
            try:
                chosen_date = date.fromisoformat(reservation_date)
                if chosen_date < date.today():
                    message = "Please choose today or a future date."
                elif reservation_slot not in SLOTS:
                    message = "Please choose a valid reservation slot."
                else:
                    with transaction.atomic():
                        if Booking.objects.filter(
                            reservation_date=chosen_date,
                            reservation_slot=reservation_slot
                        ).exists():
                            message = "Sorry, that time is already booked. Please select another slot."
                        else:
                            Booking.objects.create(
                                first_name=first_name,
                                reservation_date=chosen_date,
                                reservation_slot=reservation_slot,
                            )
                            return redirect("reservations")
            except ValueError:
                message = "Please enter a valid date."
            except IntegrityError:
                message = "Sorry, that time was just booked. Please select another slot."
    return render(request, "restaurant/book.html", {
        "today": today, "slots": SLOTS, "message": message
    })

def reservations(request):
    return render(request, "restaurant/reservations.html", {"today": date.today().isoformat()})

@require_GET
def bookings_api(request):
    date_value = request.GET.get("date")
    bookings = Booking.objects.all()
    if date_value:
        try:
            date.fromisoformat(date_value)
        except ValueError:
            return JsonResponse({"error": "Use date format YYYY-MM-DD."}, status=400)
        bookings = bookings.filter(reservation_date=date_value)
    data = [{
        "id": item.id,
        "first_name": item.first_name,
        "reservation_date": item.reservation_date.isoformat(),
        "reservation_slot": item.reservation_slot,
    } for item in bookings]
    return JsonResponse(data, safe=False)
