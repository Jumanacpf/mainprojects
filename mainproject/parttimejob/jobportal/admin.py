from django.contrib import admin
from .models import Student,Login1,Agency,Job,Application
from django.contrib.auth.models import Group,User

# Register your models here.

class AgencyAdmin(admin.ModelAdmin):
    list_display=('login_id','email','address','gender','phone')
    search_display=('login_id__username')
    list_per_page=10
    readonly_fields=('login_id','email','address','gender','phone')

class StudentAdmin(admin.ModelAdmin):
    list_display=('login_id','first_name','last_name','email','address','gender','phone','qualification')
    search_fields=('first_name','last_name')
    list_filter=('gender','qualification')
    list_per_page=10
    readonly_fields=('login_id','first_name','last_name','email','address','gender','phone','qualification')

class JobAdmin(admin.ModelAdmin):
    list_display = ('agency_id','jobname','location','salary','description')
    search_fields = ('jobname','location')
    list_filter = ('location',)
    list_per_page = 10
    readonly_fields = ('agency_id','jobname','location','salary','description')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_id','std_id','date','status','username','description')
    search_fields = ('job_id__jobname','status')
    list_filter = ('status',)
    list_per_page =10
    readonly_fields =( 'job_id','std_id','date','status','username','description')


admin.site.register(Student,StudentAdmin)
admin.site.register(Agency,AgencyAdmin)
admin.site.register(Login1)
admin.site.register(Job,JobAdmin)
admin.site.register(Application,ApplicationAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header='Part Time Job Portal'