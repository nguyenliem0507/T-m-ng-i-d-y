from django.contrib import admin
from .models import Tutor

class TutorAdmin(admin.ModelAdmin):
  list_display = ("FullName", "BirthDate", "Phone", "Email", "Gender", "Degree")
admin.site.register(Tutor, TutorAdmin)