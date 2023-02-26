from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Pending"), (1, "Confirmed"))


class Booking(models.Model):
    customer_id = models.ForeignKey(
        User, on_delete=models.Cascade, related_name='restaurant_booking')
    number_of_guests = models.IntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)
