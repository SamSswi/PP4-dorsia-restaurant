from django.shortcuts import render, HttpResponse
# https://github.com/Code-Institute-Solutions/Django3blog/tree/master/05_building_the_admin_site
# from django.views import generic
# from .models import Booking


def home_page(request):
    return render(request, 'index.html')
