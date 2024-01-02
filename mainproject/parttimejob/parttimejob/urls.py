"""parttimejob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobportal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about),
    path('contact',views.contact),
    path('jobcentre',views.job),
    path('trainer',views.trainer),
    path('std_register', views.std_register),
    path('stdedit', views.stdedit),
    path('stdview',views.stdview),
    path('agency_register', views.agency_register),
    path('aslogin', views.aslogin),
    path('aslogout',views.aslogout),
    path('addjob',views.addjob),
    path('editjob',views.editjob),
    path('jobview',views.jobview),
    path('application',views.appn)

]
