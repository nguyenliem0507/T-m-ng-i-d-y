from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('student_fullname', 'tutor_fullname', 'start_date', 'end_date')

    def student_fullname(self, obj):
        return obj.student.FullName
    student_fullname.short_description = 'Student Name'

    def tutor_fullname(self, obj):
        return obj.tutor.FullName
    tutor_fullname.short_description = 'Tutor Name'

admin.site.register(Booking, BookingAdmin)

