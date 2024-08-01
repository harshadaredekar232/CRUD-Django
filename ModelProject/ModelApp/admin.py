from django.contrib import admin
from .models import Student,Staff
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile','gender')

admin.site.register(Student,StudentAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile')

admin.site.register(Staff,StaffAdmin)