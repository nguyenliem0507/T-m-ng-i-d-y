from django.test import TestCase
from tutor.models import Tutor
from student.models import Student
from .models import Booking

class BookingModelTest(TestCase):
    def setUp(self):
        # Tạo dữ liệu cho Student và Tutor
        self.student = Student.objects.create(
            Username='admin1',
            Password='@admin123',
            FullName="Nguyen Van B",
            BirthDate="2000-05-15",
            Phone="0987654321",
            Email="student@example.com",
            Gender="Male"
        )

        self.tutor = Tutor.objects.create(
            FullName="Tran Thi C",
            BirthDate="1985-11-20",
            Phone="0123456789",
            Email="tutor@example.com",
            Gender="Female",
            Degree="Master's Degree"
        )

        # Tạo một Booking
        self.booking = Booking.objects.create(
            student=self.student,
            tutor=self.tutor,
            start_date="2025-01-01",
            end_date="2025-01-10",
            feedback="Great session!",
            approved=True
        )

    def test_booking_creation(self):
        """Test the creation of a Booking instance."""
        self.assertEqual(self.booking.student, self.student)
        self.assertEqual(self.booking.tutor, self.tutor)
        self.assertEqual(self.booking.start_date, "2025-01-01")
        self.assertEqual(self.booking.end_date, "2025-01-10")
        self.assertEqual(self.booking.feedback, "Great session!")
        self.assertTrue(self.booking.approved)

    def test_booking_str(self):
        """Test the __str__ method of Booking."""
        expected_str = "Student: Nguyen Van B - Tutor: Tran Thi C - From: 2025-01-01 to 2025-01-10"
        self.assertEqual(str(self.booking), expected_str)

    def test_related_bookings(self):
        """Test the related_name for bookings in Student and Tutor models."""
        self.assertIn(self.booking, self.student.bookings.all())
        self.assertIn(self.booking, self.tutor.bookings.all())
