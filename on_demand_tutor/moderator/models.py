from django.db import models
from on_demand_tutor.models import User 

# Create your models here.
class Moderator(User):
    def ModerateContent(self):
        pass
    