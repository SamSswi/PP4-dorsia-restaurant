# https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-login-required-decorator/
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
# https://github.com/Code-Institute-Solutions/Django3blog/tree/master/05_building_the_admin_site
from django.views import generic, View
from .models import Meal, Drink, Booking


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
        date = request.POST.get('date')
        time = request.POST.get('time')
        comment = request.POST.get('comment')
    return render(request, 'reservation.html')


def contact(request):
    return render(request, 'contact.html')
