from django.test import TestCase, Client
from django.urls import reverse
from .models import Tutor

class TutorViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_tutor_view(self):
        # Gửi request đến URL '/tutor/'
        response = self.client.get(reverse('tutor'))
        
        # Kiểm tra HTTP status code là 200
        self.assertEqual(response.status_code, 200)
        

class TutorModelTest(TestCase):
    def setUp(self):
        # Tạo một đối tượng Tutor để kiểm tra
        self.tutor = Tutor.objects.create(
            FullName="Nguyen Van A",
            BirthDate="1990-01-01",
            Phone="0123456789",
            Email="example@gmail.com",
            Gender="Male",
            Degree="Bachelor's Degree"
        )
    
    def test_tutor_str(self):
        # Kiểm tra chuỗi trả về từ phương thức __str__
        expected_str = "Nguyen Van A 1990-01-01 0123456789 example@gmail.com Male Bachelor's Degree "
        self.assertEqual(str(self.tutor), expected_str)