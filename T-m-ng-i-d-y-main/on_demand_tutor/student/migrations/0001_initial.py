# Generated by Django 5.1.4 on 2024-12-27 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('on_demand_tutor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='on_demand_tutor.user')),
            ],
            bases=('on_demand_tutor.user',),
        ),
    ]
