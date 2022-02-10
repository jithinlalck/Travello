from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def fn_Login(request):
    if request.method=='POST':
        UserName=request.POST['txtUserName']
        Password=request.POST['txtPassword']
        user=auth.authenticate(username=UserName,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login.html')

def fn_Logout(request):
    auth.logout(request)
    return redirect('/')

def fn_register(request):
    if request.method == 'POST':
        Username=request.POST['txtUserName']
        FirstName=request.POST['txtFirstName']
        LastName=request.POST['txtLastName']
        Email=request.POST['txtEmail']
        Password=request.POST['txtPassword']
        Password1=request.POST['txtPassword1']
        if Password == Password1:
            if User.objects.filter(username=Username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"mail id already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=Username,first_name=FirstName,last_name=LastName,
                                      email=Email,password=Password)
                user.save();
                # messages.info(request,"User Created")

        else:
            messages.info(request, "Passwords not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'registrationform.html')

