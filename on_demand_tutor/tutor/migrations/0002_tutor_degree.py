# Generated by Django 5.1.4 on 2025-01-06 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='Degree',
            field=models.CharField(default='B2', max_length=255),
            preserve_default=False,
        ),
    ]
