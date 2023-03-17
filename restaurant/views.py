# https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator/
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
# https://github.com/Code-Institute-Solutions/Django3blog/tree/master/05_building_the_admin_site
from django.views import generic, View
from .models import Meal, Drink, Booking
from datetime import date, timedelta, time, datetime


def home_page(request):
    return render(request, 'index.html')


def menu(request):
    meals = Meal.objects.all()
    drinks = Drink.objects.all()
    context = {'meals': meals, 'drinks': drinks}
    return render(request, 'menu.html', context)


@login_required
# class MakeReservation(View):
#     model = Booking
#     template_name = 'reservation.html'
def reservation(request):
    if request.method == 'POST':
        booking_full_name = request.POST.get('full-name')
        booking_email = request.POST.get('email')
        booking_phone_number = request.POST.get('phone_number')
        number_of_guests = request.POST.get('number_of_guests')
        booking_date_string = request.POST.get('booking-date')
        time_string = request.POST.get('booking-time')
        comment = request.POST.get('comment')
        # https://www.programiz.com/python-programming/datetime/strptime
        # https://www.geeksforgeeks.org/how-to-convert-datetime-to-date-
        # in-python/ .date() method
        booking_date = datetime.strptime(
            booking_date_string, '%Y-%m-%d').date()
        time = datetime.strptime(time_string, '%I:%M %p').time()
        Booking.objects.create(
            # https://stackoverflow.com/questions/12615154/how-to-get-the-currently-logged-in-users-user-id-in-django
            customer_id=request.user,
            booking_full_name=booking_full_name,
            booking_email=booking_email,
            booking_phone_number=booking_phone_number,
            number_of_guests=number_of_guests,
            booking_date=booking_date,
            time=time,
            comment=comment
        )
        return redirect('home_page')
    # variables
    max_guest_num = tuple(range(1, 21))
    hour_tuple = (
        '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm',
        '11:00 pm', '12:00 am', '1:00 am', '2:00 am',
        '3:00 am', '4:00 am')
    # https://stackoverflow.com/questions/1506901/cleanest-and-most-pythonic-way-to-get-tomorrows-date
    min_date = date.today() + timedelta(days=1)
    context = {
        'max_guest_num': max_guest_num,
        'hour_tuple': hour_tuple,
        'min_date': min_date}
    return render(request, 'reservation.html', context)


def contact(request):
    return render(request, 'contact.html')
