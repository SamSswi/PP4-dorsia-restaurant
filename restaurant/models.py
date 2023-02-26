from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Pending"), (1, "Confirmed"))
MEAL_TYPE = (
    (0, "Appetizer"),
    (1, "Salad"),
    (2, "Main Course"),
    (3, "Side Dish"),
    (4, "Dessert")
    )


class Booking(models.Model):
    customer_id = models.ForeignKey(
        User, on_delete=models.Cascade, related_name='restaurant_booking')
    number_of_guests = models.IntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)


class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.CharField()
    meal_type = models.IntegerField(choices=MEAL_TYPE)
    allergens = models.CharField()

    class Meta:
        ordering = ['meal_type', 'meal_name']

    def __str__(self):
        return self.meal_name
