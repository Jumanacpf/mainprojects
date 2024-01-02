from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=30, null=True)
    phone = models.IntegerField(null=True)
    qualification = models.CharField(max_length=30, null=True)
    resume = models.FileField(null=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.username

class agency(models.Model):
    agency_id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=30,null=True)
    address=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=30,)
    phone=models.IntegerField(null=True)
    password=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.username

class login1(models.Model):
    username=models.CharField(max_length=30,null=True)
    password=models.IntegerField(null=True)
    usertype=models.IntegerField(null=True)

    def __str__(self):
        return self.username

class job(models.Model):
    job_id=models.IntegerField(primary_key=True)
    job=models.CharField(max_length=30,null=True)
    location=models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.job

class application(models.Model):
    job_id=models.ForeignKey(job,on_delete=models.CASCADE,null=True)
    std_id=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    date=models.DateField(null=True)
    status=models.CharField(max_length=50,default='pending')

    def __str__(self):
        return self.status

