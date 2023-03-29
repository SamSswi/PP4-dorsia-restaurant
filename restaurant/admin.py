from django.contrib import admin
from .models import Booking, Meal, Drink
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    # The list filter variable was taken from
    # the Code Institute Codestar project
    # https://github.com/Code-Institute-Solutions/Django3blog/blob/master/05_building_the_admin_site/blog/admin.py
    list_filter = ('booking_date', 'time', 'confirmed')
    # add list_display
    actions = ['confirm_booking']

# The confirm_booking function was taken from
# the Code Institute Codestar project
# https://github.com/Code-Institute-Solutions/Django3blog/tree/master/05_building_the_admin_site
    def confirm_booking(self, request, querryset):
        querryset.update(confirmed=True)


@admin.register(Meal)
class MealAdmin(SummernoteModelAdmin):
    list_filter = ['meal_type']
    list_display = ('meal_name', 'meal_type')
    search_fields = ['meal_name', 'meal_description']


@admin.register(Drink)
class MealAdmin(SummernoteModelAdmin):
    list_filter = ['drink_type']
    list_display = ('drink_name', 'drink_type')
    search_fields = ['drink_name', 'drink_description']
