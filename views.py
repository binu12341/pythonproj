from unicodedata import name
from django.shortcuts import render,redirect
from .models import *
from hostelapp.models import Studreg
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"temp/index.html")
'''
def login(request):
    if request.method == 'POST':
        try:
            userdtl = Studreg.objects.get(susername=request.POST['uname'], spassword=request.POST['psw'])
            print("Username=",userdtl)
            request.session['uname'] = userdtl.susername
            return render(request, 'roomselection.html')
        except Studreg.DoesNotExist as e:
            messages.success(request, 'Username/Password Invalid')
            
            
    return render(request, 'temp/login.html')
    
'''

def login(request):
    return render(request,'temp/login.html')

def loginsubmit(request):
    if request.method=='POST':
        usrobj=request.POST.get("uname")
        pswdobjs=request.POST.get("psw")
        if Studreg.objects.filter(username=usrobj,password=pswdobjs).exists():
            request.session['uname']=usrobj
            request.session['psw']=pswdobjs
            user=Studreg.objects.get(susername=usrobj,spassword=pswdobjs)
            return render(request,'roomselection.html')
        else:
            messages.error(request,"username and password doesnot exist")
            return redirect(login)


def gallery(request):
    return render(request,'temp/gallery.html')

def contact(request):
    return render(request,'temp/contact.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['sname']
        password=request.POST['spass']
        address=request.POST['sadds']
        email=request.POST['semail']
        city=request.POST['scity']
        phoneno=request.POST['sphon']
        gender=request.POST['gender']
        gurdian_name=request.POST['gname']
        gurd_phoneno=request.POST['gphon']
        aadharno=request.POST['aadhar']
        Studreg(susername=username,spassword=password,sadds=address,semail=email,scity=city,sphon=phoneno,sgender=gender,sgurdianname=gurdian_name,sgurdianphon=gurd_phoneno,saadharno=aadharno).save(force_insert='__all__')
        messages.success(request, 'The New User' + " " + request.POST['sname'] + " " + 'is Saved')
        return render(request,'temp/register.html')
    else:
        return render(request,'temp/register.html')
    

def back(request):
    return render(request,'temp/index.html')

def forgotpswd(request):
    return render(request,'temp/forgetpswd.html')

def payment(request):
    return render(request,'temp/payment.html')
def roomselection(request):
    return render(request,'temp/roomselection.html')

def secureg(request):
    if request.method == 'POST':
        security_id=request.POST['sid']
        security_name=request.POST['sname']
        security_password=request.POST['spass']
        security_adds=request.POST['sadds']
        email=request.POST['semail']
        experience=request.POST['experience']
        phone=request.POST['sphon']
        security_gender=request.POST['gender']
        salary_except=request.POST['salary']
        Securityreg(security_id=security_id,security_name=security_name,security_password=security_password,security_adds=security_adds,email=email,experience=experience,phone=phone,security_gender=security_gender,salary_except=salary_except).save(force_insert='__all__')
        messages.success(request, 'The New User' + " " + request.POST['sname'] + " " + 'is Saved')
        return render(request,'temp/securityreg.html')
    else:
        return render(request,'temp/securityreg.html')


def seculoginsubmit(request):
    if request.method=='POST':
        name=request.POST.get("sname")
        pswd=request.POST.get("spass")
        if Securityreg.objects.filter(security_name=name,security_password=pswd).exists():
            request.session['sname']=name
            request.session['spass']=pswd
            user=Securityreg.objects.get(security_name=name,security_password=pswd)
            return render(request,'student_entry_exit.html')
        else:
            messages.error(request,"username and password doesnot exist")
            return redirect(login)