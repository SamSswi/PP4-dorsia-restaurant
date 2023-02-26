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
DRINK_TYPE = (
    (0, "Wine"),
    (1, "Classic Cocktail"),
    (2, "Special Cocktail"),
    (3, "Aperitif"),
    (4, "Digestif"),
    (5, "Sparkling Wine"),
    (6, "Beer")
    )


class Booking(models.Model):
    customer_id = models.ForeignKey(
        User, on_delete=models.Cascade, related_name='restaurant_booking')
    number_of_guests = models.IntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)

# add __str__ to bookings


class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.CharField()
    meal_type = models.IntegerField(choices=MEAL_TYPE)
    allergens = models.CharField()

    class Meta:
        ordering = ['meal_type', 'meal_name']

    def __str__(self):
        return self.meal_name


class Drink(model.Models):
    drink_name = models.CharField(max_length=80)
    drink_description = models.CharField()
    drink_type = models.IntegerField(choices=DRINK_TYPE)
    allergens = model.CharField()

    class Meta:
        ordering = ['drink_type', 'drink_name']

    def __str__(self):
        return self.drink_name
