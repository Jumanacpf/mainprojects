from django.contrib import admin
from .models import Student,login1,agency,job,application

# Register your models here.
admin.site.register(Student)
admin.site.register(agency)
admin.site.register(login1)
admin.site.register(job)
admin.site.register(application)