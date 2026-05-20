from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from todo import models
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return redirect('todopage')
    return redirect('signup')


def signup(request):
    if request.user.is_authenticated:
        return redirect('todopage')

    if request.method == 'POST':
        fnm = request.POST.get('fnm', '').strip()
        emailid = request.POST.get('email', '').strip()
        pwd = request.POST.get('pwd', '')

        if User.objects.filter(username=fnm).exists():
            messages.error(request, 'Username already exists. Please choose another username.')
            return redirect('signup')

        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')
    
    return render(request, 'signup.html')
          

def loginn(request):
    if request.user.is_authenticated:
        return redirect('todopage')

    if request.method == 'POST':
        fnm = request.POST.get('fnm', '').strip()
        pwd = request.POST.get('pwd', '')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            auth_login(request, userr)
            return redirect('todopage')

        messages.error(request, 'Invalid username or password.')
        return redirect('login')
               
    return render(request, 'login.html')
        
@login_required(login_url='/login/')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            obj = models.TODOO(title=title, user=request.user)
            obj.save()
        return redirect('todopage')
        
    res = models.TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})

@login_required(login_url='/login/')
def delete_todo(request,srno):
    obj = get_object_or_404(models.TODOO, srno=srno, user=request.user)
    obj.delete()
    return redirect('todopage')

@login_required(login_url='/login/')
def edit_todo(request, srno):
    obj = get_object_or_404(models.TODOO, srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            obj.title = title
            obj.save()
        return redirect('todopage')

    return render(request, 'edit_todo.html', {'obj': obj})


def signout(request):
    logout(request)
    return redirect('login')
