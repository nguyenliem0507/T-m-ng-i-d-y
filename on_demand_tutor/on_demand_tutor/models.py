from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    Username = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    FullName = models.CharField(max_length=255)
    BirthDate = models.DateField()
    Gender = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
        ],
    )
    Phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be 10 digits',
            )
        ],
    )
    Email = models.EmailField(max_length=255)