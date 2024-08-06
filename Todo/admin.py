from django.contrib import admin

from .models import Students
# Register your models here.

class StudentAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'enrolled_date')
    

admin.site.register(Students, StudentAdmin)