from django.db import models

# Create your models/DB tables here.

class StudentInfo(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    major = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    
class CourseInfo(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=100)
    coursename = models.CharField(max_length=100)
    studentsenrolled = models.IntegerField()
    coursedepartment = models.CharField(max_length=100)
    instructorfullname = models.CharField(max_length=100)
    
class EnrollmentInfo(models.Model):
        studentname = models.CharField(max_length=100)
        coursename = models.CharField(max_length=100)
    
    
