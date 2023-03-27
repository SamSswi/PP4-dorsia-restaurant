# https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator/
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
# https://github.com/Code-Institute-Solutions/Django3blog/tree/master/05_building_the_admin_site
from django.views import generic, View
from .models import Meal, Drink, Booking
from datetime import date, timedelta, time, datetime
from django.contrib import messages


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
        messages.success(request, 'You have successfully made a reservation')
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


def manage_reservations(request):
    username = request.user
    bookings = Booking.objects.filter(
        customer_id=username).order_by('-booking_date')
    context = {'bookings': bookings, 'username': username}
    return render(request, 'manage_reservations.html', context)


def edit_reservation(request, booking_id):
    booking_to_edit = Booking.objects.get(id=booking_id)
    # https://stackoverflow.com/questions/14619494/how-to-understand-strptime-vs-strftime#:~:text=strptime%20is%20short%20for%20%22parse,seen%20strptime%20used%20since%20DateTime.
    booking_date_str = booking_to_edit.booking_date.strftime('%Y-%m-%d')
    time_str_am = booking_to_edit.time.strftime('%-I:%M %p').replace(
        'am', ' am').lower()
    time_str = time_str_am.replace('pm', 'pm').lower()
    if request.method == 'POST':
        booking_full_name = request.POST.get('full-name')
        booking_email = request.POST.get('email')
        booking_phone_number = request.POST.get('phone_number')
        number_of_guests = int(request.POST.get('number_of_guests'))
        booking_date_string = request.POST.get('booking-date')
        time_string = request.POST.get('booking-time')
        comment = request.POST.get('comment')
        booking_date = datetime.strptime(
            booking_date_string, '%Y-%m-%d').date()
        time = datetime.strptime(time_string, '%I:%M %p').time()
        # Update the blog post object with the new values
        booking_to_edit.booking_full_name = booking_full_name
        booking_to_edit.booking_email = booking_email
        booking_to_edit.booking_phone_number = booking_phone_number
        booking_to_edit.number_of_guests = number_of_guests
        booking_to_edit.booking_date = booking_date
        booking_to_edit.time = time
        booking_to_edit.comment = comment
        booking_to_edit.save()
        messages.success(
            request,
            'You have successfully made changes to the reservation')
        return redirect('manage_reservations')
    # variables
    hour_tuple = (
        '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm',
        '11:00 pm', '12:00 am', '1:00 am', '2:00 am',
        '3:00 am', '4:00 am')
    max_guest_num = tuple(range(1, 21))
    min_date = date.today() + timedelta(days=1)
    context = {
        'max_guest_num': max_guest_num,
        'booking_to_edit': booking_to_edit,
        'booking_date_str': booking_date_str,
        'time_str': time_str,
        'hour_tuple': hour_tuple,
        'min_date': min_date}
    return render(request, 'edit_reservation.html', context)


def delete_reservation(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == "POST":
        booking.delete()
        messages.success(
            request,
            'You have successfully deleted the reservation')
        return redirect('manage_reservations')
    context = {'booking': booking}
    return render(request, 'delete_reservation.html', context)
