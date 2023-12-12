from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'ERROR! Invalid Credential')
            return redirect('home')
    else:
        return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged Out...')
    return redirect('home')


def student_page(request):
    if request.user.is_authenticated:
        return render(request, 'student_page.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')

def courses_page(request):
    if request.user.is_authenticated:
        return render(request, 'courses_page.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')

def schemes_page(request):
    if request.user.is_authenticated:
        return render(request, 'schemes_page.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")

def state_page(request):
    if request.user.is_authenticated:
        return render(request, 'state_page.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")

def college_page(request):
    if request.user.is_authenticated:
        return render(request, 'college_page.html', {})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")
