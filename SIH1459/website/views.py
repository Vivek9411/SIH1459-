from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import State, Scheme, Course, College
from .forms import AddSchemeForm, AddCourseForm


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
    course_records = Course.objects.all()
    if request.user.is_authenticated:
        return render(request, 'courses_page.html', {'course_records': course_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect('home')


def schemes_page(request):
    scheme_records = Scheme.objects.all()
    if request.user.is_authenticated:
        return render(request, 'schemes_page.html', {'scheme_records': scheme_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")


def state_page(request):
    state_records = State.objects.all()
    if request.user.is_authenticated:
        return render(request, 'state_page.html', {'state_records': state_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")


def college_page(request):
    college_records = College.objects.all()
    if request.user.is_authenticated:
        return render(request, 'college_page.html', {'college_records': college_records})
    else:
        messages.success(request, 'Please log in first')
        return redirect("home")


def add_scheme(request):
    form = AddSchemeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Scheme Added')
                return redirect('schemes_page')
        return render(request, 'add_scheme.html', {'form': form})
    else:
        messages.success(request, 'You must be loggedin')
        return redirect('home')


def add_course(request):
    form = AddCourseForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Course Added')
                return redirect('courses_page')
        return render(request, 'add_course.html', {'form': form})
    else:
        messages.success(request, 'You must be loggedin')
        return redirect('home')
