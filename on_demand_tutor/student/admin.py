from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
  list_display = ("FullName", "BirthDate", "Phone","Email")
admin.site.register(Student, StudentAdmin)