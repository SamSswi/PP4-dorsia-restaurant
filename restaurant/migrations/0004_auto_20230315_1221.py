# Generated by Django 3.2.18 on 2023-03-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_booking_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_full_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
