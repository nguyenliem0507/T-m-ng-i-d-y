from django.db import models
from on_demand_tutor.models import User  

class Tutor(User):
    def CreateService(self):
        pass
    def UploadContent(self):
        pass
    def __str__(self):
        return f"{self.FullName} {self.BirthDate} {self.Phone} {self.Email}"
    
