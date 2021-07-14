from django.db import models
from django.forms import ModelForm

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(verbose_name='First name of the student', max_length=32)
    last_name = models.CharField(verbose_name='Last name of the student', max_length=32)
    hometown = models.CharField(verbose_name='Home town', max_length=32)
    age = models.IntegerField(verbose_name='Age of the student')
    linkedin_profile = models.CharField(verbose_name="LinkedIn profile link", max_length=256, default="https://www.linkedin.com/")

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'hometown', "age", "linkedin_profile"]

class Course(models.Model):
    title = models.CharField(verbose_name="Title of the course", max_length=32)
    instructor = models.CharField(verbose_name="Instructor of the course", max_length=32)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.title + " by " + self.instructor
    

