from django.contrib.auth.models import User
from .models import Booking
from django.test import TestCase
from datetime import datetime, timedelta, date


class TestViews(TestCase):
    def setUp(self):
        # The solution on how to create a test user was found on:
        # https://stackoverflow.com/questions/36940384/how-do-i-setup-a-unit-test-user-for-django-app-the-unit-test-cant-login
        self.user = User.objects.create_user(
            username='testuser', password='TestPassword12345')

    # The home page test function was taken from
    # the Code Institute Hello Django sample project
    # https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/5666926980b74689b37a0d5da3cec510/
    def test_get_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_menu_page(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_get_reservation_page(self):
        # The login line was taken from Stackoverflow:
        # https://stackoverflow.com/questions/36940384/how-do-i-setup-a-unit-test-user-for-django-app-the-unit-test-cant-login
        self.client.login(username='testuser', password='TestPassword12345')
        response = self.client.get('/reservation/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation.html')

    def test_get_manage_reservations_page(self):
        self.client.login(username='testuser', password='TestPassword12345')
        response = self.client.get('/manage_reservations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage_reservations.html')

    def test_get_edit_reservation_page(self):
        self.client.login(username='testuser', password='TestPassword12345')
        booking = Booking.objects.create(
            customer_id=self.user,
            booking_full_name='Test User',
            booking_email='test@email.com',
            booking_phone_number='0648425841',
            number_of_guests=15,
            booking_date=datetime.now()+timedelta(days=10),
            time='10:00 PM',
            comment='Test Comment'
        )
        response = self.client.get(f'/edit_reservation/{booking.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_reservation.html')

    def test_get_delete_reservation(self):
        self.client.login(username='testuser', password='TestPassword12345')
        booking = Booking.objects.create(
            customer_id=self.user,
            booking_full_name='Test User',
            booking_email='test@email.com',
            booking_phone_number='0648425841',
            number_of_guests=15,
            booking_date=datetime.now()+timedelta(days=10),
            time='10:00 PM',
            comment='Test Comment'
        )
        response = self.client.get(f'/delete_reservation/{booking.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_reservation.html')

    def test_can_make_reservation(self):
        self.client.login(username='testuser', password='TestPassword12345')
        response = self.client.post('/reservation/', {
            'customer_id': self.user.id,
            'booking_full_name': 'Test User',
            'booking_email': 'test@email.com',
            'booking_phone_number': '0648425841',
            'number_of_guests': 15,
            'booking-date': '2040-11-11',
            'booking-time': '10:00 PM',
            'comment': 'Test Comment',
        })
        self.assertRedirects(response, '/')

    def test_can_delete_reservation(self):
        self.client.login(username='testuser', password='TestPassword12345')
        booking = Booking.objects.create(
            customer_id=self.user,
            booking_full_name='Test User',
            booking_email='test@email.com',
            booking_phone_number='0648425841',
            number_of_guests=15,
            booking_date=datetime.now()+timedelta(days=10),
            time='10:00 PM',
            comment='Test Comment'
        )
        response = self.client.post(f'/delete_reservation/{booking.id}/', {})
        self.assertRedirects(response, '/manage_reservations/')
        existing_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(existing_bookings), 0)

    def test_can_edit_reservation(self):
        self.client.login(username='testuser', password='TestPassword12345')
        booking = Booking.objects.create(
            customer_id=self.user,
            booking_full_name='Test User',
            booking_email='test@email.com',
            booking_phone_number='0648425841',
            number_of_guests=15,
            booking_date=datetime.now()+timedelta(days=10),
            time='10:00 PM',
            comment='Test Comment'
        )
        response = self.client.post(f'/edit_reservation/{booking.id}/', {
            'customer_id': self.user.id,
            'booking_full_name': 'Test User1',
            'booking_email': 'test1@email.com',
            'booking_phone_number': '0648457871',
            'number_of_guests': 1,
            'booking-date': '2040-11-12',
            'booking-time': '11:00 PM',
            'comment': 'Test Comment 1',
        })
        self.assertRedirects(response, '/manage_reservations/')
