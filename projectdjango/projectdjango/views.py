from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app.models import Useradd,Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request,"base.html",{})

def contact(request):
    return render(request,"contact.html",{})

def ferrari(request):
    return render(request,"ferrari.html",{})

def rangeover(request):
    return render(request,"rangeover.html",{})

    

def login_user(request):
    if request.method=="POST":
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        user= authenticate(Username=Username, Password=Password)
        if user is not None:

            login(request,user)
        
        return redirect("home")

    return render(request,"login.html",{})
def register(request):
    if request.method=="POST":
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        Email=request.POST.get("Email")
        c = User.objects.create_user(Username=Username,Email=Email,Password=Password) 
        c.save()
        return redirect("login")
    
    return render(request,"register.html",{})

def logout_user(request):
    logout(request)
    return redirect("login")




def contact(request):
    if request.method=="POST":
        Name=request.POST['Name']
        Email=request.POST['Email']
        Message=request.POST['Message']
        Phone=request.POST['Phone']
        Subject=request.POST['Subject']


        c=Contact(Name=Name,Email=Email,Message=Message,Phone=Phone,Subject=Subject)
        c.save()
        return redirect("home")

    return render(request,"contact.html",{})

def error_404(request,exception):
    return render(request,"base.html")    

