from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path("student_page", views.student_page, name='student_page'),
    path("courses_page", views.courses_page, name='courses_page'),
    path("schemes_page", views.schemes_page, name='schemes_page'),
    path("state_page", views.state_page, name='state_page'),
    path("college_page", views.college_page, name='college_page'),

]
