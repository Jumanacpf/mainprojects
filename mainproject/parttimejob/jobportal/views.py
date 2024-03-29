from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .models import Agency
from .models import Login1
from .models import Job
from .models import Application


# Create your views here.

def stdhome(request):
    return render(request,'student/stdhome.html')

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
            data = Login1.objects.create(username=username,
                                         password=password,
                                         usertype=1)
            data.save()
            details=Student.objects.create(
                                           login_id=data,
                                           first_name=first_name,
                                           last_name=last_name,
                                           email=email,
                                           address=address,
                                           gender=gender,
                                           phone=phone,
                                           qualification=qualification,
                                           resume=resume)
            details.save()
            return redirect(aslogin)
            # return render(request, 'agency_reg.html', {'register': 'You are Registered'})
        except Exception as e:
            return HttpResponse(e)
    else:
        return render(request,'student/std_reg.html')

def stdedit(request):
    id=request.session['id']
    user=Login1.objects.get(id=id)
    std=Student.objects.get(login_id=user.id)
    if request.method == 'POST':
        std.first_name = request.POST['first_name']
        std.last_name = request.POST['last_name']
        std.email = request.POST['email']
        std.address = request.POST['address']
        std.gender = request.POST['gender']
        std.phone = request.POST['phone']
        std.qualification = request.POST['qualification']

        if std.resume == request.FILES:
            std.resume=request.FILES['image']
        std.save()



        return render(request,'student/stdhome.html')
    else:
        return render(request, 'student/stdedit.html',{'std':std})

def stdview(request):
    if 'id' in request.session:
        user_id=request.session['id']
        data=Login1.objects.get(id=user_id)
        user=Student.objects.get(login_id=data.id)
        return render(request,'student/stdview.html',{'data':user})
    else:
        return render(request,'login.html')

def jobsearch(request):
    if request.method=='POST':
        jobname=request.POST['jobname']
        data=Job.objects.filter(jobname__icontains=jobname)
        return render(request,'student/jobview.html',{'data':data})
    else:
        return render(request,'student/jobview.html')


def jobnotapplied(request):
    id = request.session['id']
    login_data = Login1.objects.get(id=id)
    stddet = Student.objects.filter(login_id=login_data)
    applied_data=Application.objects.filter(std_id=stddet,status='approved').values_list('job_id',flat=True)
    data=Job.objects.exclude(application__status='approved')
    return render(request,'student/jobview.html',{'data':data})

def job_applications(request,jobid):
    id = request.session['id']
    login_data = Login1.objects.get(id=id)
    user = Student.objects.get(login_id=login_data)
    work = Job.objects.get(id=jobid)
    return render(request, 'student/jobapplied.html',{'work':work})

def job_applied(request,jobid):
    id = request.session['id']
    login_data = Login1.objects.get(id=id)
    user=Student.objects.get(login_id=login_data)
    work=Job.objects.get(id=jobid)
    if request.method == 'POST':
        description = request.POST['description']
        data=Application.objects.create(job_id=work,
                                        std_id=user,
                                        description=description)
        data.save()
        if Application.objects.filter(std_id=user).exists():

            return render(request, 'student/jobapplied.html', {'apply': 'you are applied','work':work})
        # else:
            # return render(request, 'student/jobapplied.html')
    else:
        return render(request, 'student/jobapplied.html')

def stdreview(request):
    id=request.session['id']
    reviewdata=Login1.objects.get(id=id)
    user=Student.objects.get(login_id=reviewdata)
    data=Application.objects.filter(std_id=user)
    return render(request,'student/stdreview.html',{'data':data})



def agencyhome(request):
    return render(request,'agency/agencyhome.html')

def agency_register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        password=request.POST['password']
        images=request.FILES['images']

        # if Login1.objects.filter(username=username).exists():
        #     return render(request,'register.html',{'name_error':'Username already exists'})
        # if Agency.objects.filter(email=email).exists():
        #     return render(request,'register.html',{'email_error':'Email already exists'})


        data=Login1.objects.create(username=username,
                                   password=password,
                                   usertype=0)
        data.save()
        details=Agency.objects.create(
                                      login_id=data,
                                      email=email,
                                      address=address,
                                      phone=phone,
                                      image=images)
        details.save()
        return redirect(aslogin)

    else:
        return render(request,'agency/agency_reg.html')

def agencyview(request):
    if 'id' in request.session:
        user_id=request.session['id']
        data=Login1.objects.get(id=user_id)
        user=Agency.objects.get(login_id=data.id)
        return render(request,'agency/agencyview.html',{'data':user})
    else:
        return render(request,'login.html')

def agencyedit(request):
    id=request.session['id']
    user=Login1.objects.get(id=id)
    datas=Agency.objects.get(login_id=user)
    if request.method == 'POST':
        datas.email = request.POST['email']
        datas.address = request.POST['address']
        datas.phone = request.POST['phone']
        datas.save()

        return render(request,'agency/agencyhome.html')
    else:
        return render(request, 'agency/agencyedit.html',{'datas':datas})

def aslogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=int(request.POST['password'])
        data = Login1.objects.get(username=username)
        if data.password == password:
            request.session['id'] = data.id
            if data.usertype == 0:
                return render(request,'agency/agencyhome.html')
            elif data.usertype == 1:
                return render(request,'student/stdhome.html')
            else:
                return HttpResponse("loggined")
        else:
            return render(request, 'login.html',{'error':'Invalid Credential'})
    else:
        return render(request,'login.html')

def addjob(request):
    id = request.session['id']
    login_data = Login1.objects.get(id=id)
    user = Agency.objects.get(login_id=login_data)
    if request.method=='POST':
        jobs=request.POST['jobs']
        location=request.POST['location']
        salary=request.POST['salary']
        description=request.POST['description']
        data=Job.objects.create(agency_id=user,jobname=jobs,location=location,salary=salary,description=description)
        data.save()
        return redirect(agencyhome)
    else:
        return render(request,'agency/job.html')

def editjob(request,jobid):
    id=request.session['id']
    login_data=Login1.objects.get(id=id)
    user = Agency.objects.get(login_id=login_data)
    datas=Job.objects.get(id=jobid)
    print(datas)

    if request.method=='POST':
        jobs=request.POST['job']
        location=request.POST['loc']
        salary=request.POST['salary']
        description=request.POST['description']
        datas.jobname=jobs
        datas.location=location
        datas.salary=salary
        datas.description=description
        datas.save()
        return redirect(jobaview)
    else:
        return render(request,'agency/editjob.html',{'datas':datas})

def jobaview(request):
    id=request.session['id']
    login_data=Login1.objects.get(id=id)
    user = Agency.objects.get(login_id=login_data)
    data= Job.objects.filter(agency_id=user)
    print(data)
    return render(request,'agency/jobaview.html',{'data':data})

def applicationrequest(request,id):
    data=Application.objects.get(id=id)
    if request.method=='POST':
        application=request.POST['application']
        if application=='accepted':
            data.status='approved'
        elif application=='rejected':
            data.status='rejected'
        elif application=='completed':
            data.status='completed'
        data.save()
        return redirect(requestview)

def delete(request,jobid):
    id = request.session['id']
    data = Login1.objects.get(id=id)
    user = Agency.objects.get(login_id=data)
    user = Job.objects.filter(id=jobid)
    user.delete()
    return redirect(jobaview)

def requestview(request):
    id = request.session['id']
    login_data = Login1.objects.get(id=id)
    agencydet = Agency.objects.get(login_id=login_data)
    user = Job.objects.filter(agency_id=agencydet)
    allapplication=Application.objects.filter(job_id__agency_id=agencydet).order_by('date')
    print(allapplication)
    return render(request,'agency/request.html',{'allapplication':allapplication})


def history(request):
    id = request.session['id']
    login_data = Login1.objects.get(id=id)
    agencydet=Agency.objects.get(login_id=login_data)
    user =Job.objects.filter(agency_id=agencydet)
    allapplication=Application.objects.filter(status='approved',job_id__agency_id=agencydet)
    return render(request,'agency/history.html',{'allapplication':allapplication})



def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')




def aslogout(request):
    # if 'id' in request.session:
        request.session.flush()
        return redirect(index)
    # else:
    #     return HttpResponse("logout")