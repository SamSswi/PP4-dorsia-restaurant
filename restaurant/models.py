from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
        User, on_delete=models.CASCADE, related_name='restaurant_booking')
    booking_full_name = models.CharField(max_length=100, null=True)
    booking_email = models.EmailField(null=True)
    booking_phone_number = models.CharField(max_length=20, null=True)
    number_of_guests = models.IntegerField(default=1)
    booking_date = models.DateField()
    time = models.TimeField()
    comment = models.TextField(default='')
    # https://github.com/Code-Institute-Solutions/Django3blog/blob/master/05_building_the_admin_site/blog/models.py
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.booking_full_name} - {self.booking_date}, {self.time}; {self.number_of_guests}guests"


class Meal(models.Model):
    meal_name = models.CharField(max_length=100)
    meal_description = models.CharField(max_length=1000)
    meal_type = models.IntegerField(choices=MEAL_TYPE)
    allergens = models.CharField(max_length=250)

    class Meta:
        ordering = ['meal_type', 'meal_name']

    def __str__(self):
        return self.meal_name


class Drink(models.Model):
    drink_name = models.CharField(max_length=80)
    drink_description = models.CharField(max_length=1000)
    drink_type = models.IntegerField(choices=DRINK_TYPE)
    allergens = models.CharField(max_length=250)

    class Meta:
        ordering = ['drink_type', 'drink_name']

    def __str__(self):
        return self.drink_name
