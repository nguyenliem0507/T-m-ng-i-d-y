from django.contrib import admin
from .models import Tutor

class TutorAdmin(admin.ModelAdmin):
  list_display = ("FullName", "BirthDate", "Phone","Email")
admin.site.register(Tutor, TutorAdmin)