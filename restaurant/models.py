from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.CharField(max_length=20)

    class Meta:
        ordering = ["reservation_date", "reservation_slot"]
        constraints = [models.UniqueConstraint(fields=["reservation_date", "reservation_slot"], name="unique_booking_date_slot")]

    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} at {self.reservation_slot}"
