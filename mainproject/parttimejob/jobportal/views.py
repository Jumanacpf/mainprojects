from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .models import agency
from .models import login1
from .models import job
from .models import application


# Create your views here.

def std_register(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        gender=request.POST['gender']
        phone=request.POST['phone']
        qualification=request.POST['qualification']
        resume=request.FILES['image']
        password = request.POST['password']
        try:
            details=Student.objects.create(
                                           first_name=first_name,
                                           last_name=last_name,
                                           username=username,
                                           email=email,
                                           address=address,
                                           gender=gender,
                                           phone=phone,
                                           qualification=qualification,
                                           resume=resume,
                                           password=password)
            details.save()

            data = login1.objects.create(username=username,
                                         password=password,
                                         usertype=1)
            data.save()
            return render(request, 'agency_reg.html', {'register': 'You are Registered'})
        except Exception as e:
            return HttpResponse("Username already exists. Please choose a different username.")
    else:
        return render(request,'std_reg.html')

def stdedit(request):
    if request.method == 'POST':
        std_id = int(request.POST['std_id'])
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        gender = request.POST['gender']
        phone = request.POST['phone']
        qualification = request.POST['qualification']
        resume = request.FILES['image']
        password = request.POST['password']
        detail = Student.objects.filter(id=std_id).update(first_name=first_name,
                                                          last_name=last_name,
                                                          username=username,
                                                          email=email,
                                                          address=address,
                                                          gender=gender,
                                                          phone=phone,
                                                          qualification=qualification,
                                                          resume=resume,
                                                          password=password)
        return render(request, 'stdedit.html', {'edit': 'Edit profile successfully'})
    else:
        return render(request, 'stdedit.html')

def stdview(request):
    if 'id' in request.session:
        id=request.session['id']

        data=Student.objects.get(id=id)
        print(data)
        return render(request,'stdview.html',{'data':data})

    else:
        return redirect(aslogin)

def agency_register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        password=request.POST['password']
        details=agency.objects.create(username=username,
                                      email=email,
                                      address=address,
                                      phone=phone,
                                      password=password)
        details.save()

        data=login1.objects.create(username=username,
                                   password=password,
                                   usertype=0)
        data.save()
        return redirect(aslogin)
        # return render(request,'agency_reg.html',{'register':'You are Registered'})
    else:
        return render(request,'agency_reg.html')



def aslogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        data = login1.objects.get(username=username)
        print(data)
        if data.password == password:
            request.session['id'] = data.id
            if data.usertype == 0:
                return HttpResponse("agency login")
            elif data.usertype == 1:
                return HttpResponse("student login")
        else:
            return render(request, 'login.html',{'success':'You are  not loggined'})
    else:
        return render(request,'login.html')
def addjob(request):
    if request.method=='POST':
        jobs=request.POST['job']
        location=request.POST['location']
        data=job.objects.create(job=jobs,location=location)
        data.save()

        return render(request,'job.html',{'added':'job added'})
    else:
        return render(request,'job.html')

def editjob(request):
    if request.method=='POST':
        job_id=int(request.POST['job_id'])
        jobs=request.POST['job']
        location=request.POST['loc']
        data=job.objects.filter(job_id=job_id).update(job=jobs,location=location)

        return render(request, 'editjob.html',{'edit':'Edit job successfully'})
    else:
        return render(request,'editjob.html')


def jobview(request):
    data=job.objects.all()
    return render(request,'jobview.html',{'data':data})


def appn(request):
    if request.method=='POST':
        date=request.POST['date']
        status=request.POST['status']
        data=application.objects.create(date=date,
                                        status=status)
        data.save()
        return render(request, 'application.html',{'application':'applied successfully'})
    else:
        return render(request,'application.html')

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def jobcentre(request):
    return render(request,'service.html')
def trainer(request):
    return render(request,'guard.html')

def aslogout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(index)
    else:
        return HttpResponse("logout")