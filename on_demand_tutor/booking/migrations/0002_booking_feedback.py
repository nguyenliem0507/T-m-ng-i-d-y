# Generated by Django 5.1.4 on 2025-01-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
