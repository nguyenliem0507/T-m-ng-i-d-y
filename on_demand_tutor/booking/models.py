from django.db import models
from tutor.models import Tutor
from student.models import Student

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='bookings')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Student: {self.student.FullName} - Tutor: {self.tutor.FullName} - From: {self.start_date} to {self.end_date}"

