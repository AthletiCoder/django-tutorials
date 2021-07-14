from django.shortcuts import render, redirect
from .models import Student, StudentForm
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def list_all(request):
    all_students = Student.objects.all()
    template_name = "students.htm"
    arguments = {"students": all_students}
    return render(request, template_name, context=arguments)

@csrf_exempt
def enroll_student(request):
    context ={}
  
    # create object of form
    form = StudentForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect("/students/list-all")
  
    context['form']= form
    return render(request, "enroll_student.htm", context)