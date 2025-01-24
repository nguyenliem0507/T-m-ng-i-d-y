from django.test import TestCase, Client
from django.urls import reverse


class StudentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_tutor_view(self):
        # Gửi request đến URL '/tutor/'
        response = self.client.get(reverse('student'))
        
        # Kiểm tra HTTP status code là 200
        self.assertEqual(response.status_code, 200)