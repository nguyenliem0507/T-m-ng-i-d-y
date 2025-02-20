from django.db import models
from on_demand_tutor.models import User  

class Student(User):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
