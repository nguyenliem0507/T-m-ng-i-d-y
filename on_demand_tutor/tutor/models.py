from django.db import models
from on_demand_tutor.models import User  

class Tutor(User):
    Degree = models.CharField(max_length=255)
    def CreateService(self):
        pass
    def UploadContent(self):
        pass
    def __str__(self):
        return f"{self.FullName} {self.BirthDate} {self.Phone} {self.Email} {self.Gender} {self.Degree} "
    
class Feedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks', limit_choices_to={'groups__name': 'Student'})
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_received', limit_choices_to={'groups__name': 'Tutor'})
    content = models.TextField()  # Nội dung phản hồi
    start_date = models.DateField()  # Ngày bắt đầu
    end_date = models.DateField()  # Ngày kết thúc
    is_approved = models.BooleanField(default=False)  # Trạng thái phê duyệt
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.student.username} to {self.tutor.username}"
