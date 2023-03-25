"""dorsia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from restaurant.views import home_page, menu, reservation, manage_reservations, edit_reservation, delete_reservation
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', home_page, name='home_page'),
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation'),
    path(
        'manage_reservations/',
        manage_reservations,
        name='manage_reservations'),
    path(
        'edit_reservation/<int:booking_id>/',
        edit_reservation, name='edit_reservation'),
    path(
        'delete_reservation/<int:booking_id>/',
        delete_reservation, name='delete_reservation'),
    path('accounts/', include('allauth.urls')),
]
