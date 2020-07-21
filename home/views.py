from django.shortcuts import render,redirect
from .models import Contact
from datetime import datetime
from django.contrib.auth import authenticate, login as dj_login,logout as dj_logout
from django.contrib.auth.models import User

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request,user)
            # Redirect to a success page.
            return redirect('/')
        else:
        # Return an 'invalid login' error message.
            return render(request,'login.html')
        # Return an 'invalid login' error message.
    return render(request,'login.html')

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    else:
        return render(request,'index.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        decr = request.POST.get('decr')
        contact = Contact(name=name,number=number,email=email,decr=decr,date=datetime.today() )
        contact.save()
    return render(request,'contact.html')

def logout(request):
    dj_logout(request)
    return redirect('/login')
