from atexit import register
import imp
from django.contrib import admin
from myapp import models
from .models import Resume


# Register your models here.
# id=pass=tankman

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob', 'gender', 'locality', 'city',
                    'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
