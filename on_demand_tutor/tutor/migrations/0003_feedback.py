# Generated by Django 5.1.5 on 2025-01-19 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('on_demand_tutor', '0002_user_role'),
        ('tutor', '0002_tutor_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(limit_choices_to={'groups__name': 'Student'}, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='on_demand_tutor.user')),
                ('tutor', models.ForeignKey(limit_choices_to={'groups__name': 'Tutor'}, on_delete=django.db.models.deletion.CASCADE, related_name='feedback_received', to='on_demand_tutor.user')),
            ],
        ),
    ]
