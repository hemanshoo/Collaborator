from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User
from hashlib import sha256

def login(request):
    if 'username' not in request.session:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.filter(username=username).first()
            if user:
                if user.password == sha256(password.encode('utf-8')).hexdigest():
                    request.session['username'] = user.username
                    return redirect('login-home')
            else:
                context={'message':'User not found'}
                return render(request,'login/login.html',context)
        return render(request, 'login/login.html')
    return redirect('login-home')

def signup(request):
    if 'username' not in request.session:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            confirm_password = request.POST['confirm']
            if password == confirm_password:
                password = sha256(password.encode('utf-8')).hexdigest()
                new_user = User(username = username, password = password)
                new_user.save()
                return redirect('login-home')
            else:
                context = {'message': "Passwords don't match"}
                return render(request,'login/signup.html',context)
        return render(request, 'login/signup.html')
    return redirect('login-home')


def home(request):
    if 'username' not in request.session:
        return redirect('login-login')
    else:
        context = {'username':request.session['username']}
        return render(request,'login/home.html',context)

def logout(request):
    if 'username' not in request.session:
        return redirect('login-login')
    else:
        request.session.flush()
        return redirect('login-login')

