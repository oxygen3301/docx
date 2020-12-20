from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import LogForm
from .models import Log
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'patient/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'patient/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'patient/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'patient/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'patient/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'patient/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')
            
def loginhospital(request):
    if request.method == 'GET':
        return render(request, 'patient/loginhospital.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'patient/loginhospital.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def createlog(request):
    if request.method == 'GET':
        return render(request, 'patient/createlog.html', {'form':LogForm()})
    else:
        try:
            form = LogForm(request.POST)
            newlog = form.save(commit=False)
            newlog.save()
            return redirect('home')
        except ValueError:
            return render(request, 'patient/createlog.html', {'form':LogForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def viewlogs(request):
    logs = Log.objects.filter(user=request.user)
    return render(request, 'patient/viewlogs.html', {'logs':logs})

@login_required
def viewlog(request, log_pk):
    log = get_object_or_404(Log, pk=log_pk, user=request.user)
    if request.method == 'GET':
        form = LogForm(instance=log)
        return render(request, 'patient/viewlog.html', {'log':log, 'form':form})
    else:
        try:
            form = LogForm(request.POST, instance=log)
            form.save()
            return redirect('viewlogs')
        except ValueError:
            return render(request, 'patient/viewlog.html', {'log':log, 'form':form, 'error':'Bad info'})
