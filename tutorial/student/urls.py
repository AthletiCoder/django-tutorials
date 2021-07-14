from django.contrib import admin
from django.urls import path, include
from .views import list_all, enroll_student

urlpatterns = [
    path('list-all/', list_all, name='list_all'),
    path('enroll-student/', enroll_student, name='enroll_student')
]
