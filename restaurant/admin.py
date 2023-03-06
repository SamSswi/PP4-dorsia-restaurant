from django.contrib import admin
from .models import Booking, Meal, Drink
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    # https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/09e0a94c7dbd4b969b8358a0cf5660b2/?child=first
    list_filter = ('status', 'date', 'time')
    # add list_display
    actions = ['confirm_booking']

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
