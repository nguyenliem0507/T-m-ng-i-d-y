# Generated by Django 5.1.4 on 2025-01-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_booking_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
