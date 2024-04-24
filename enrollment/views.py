from django.shortcuts import render
from enrollment.models import StudentInfo, CourseInfo, EnrollmentInfo
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

#def login (request):
    #return render(request, "enrollment/home.html")
 

@login_required
def home(request):
    freshman = StudentInfo.objects.filter(year='Freshman').count()
    sophomore = StudentInfo.objects.filter(year='Sophomore').count()
    junior = StudentInfo.objects.filter(year='Junior').count()
    senior = StudentInfo.objects.filter(year='Senior').count()
    
    physics= StudentInfo.objects.filter(major='Physics').count()
    it = StudentInfo.objects.filter(major='I.T.').count()
    chemistry = StudentInfo.objects.filter(major='Chemistry').count()
    marketing = StudentInfo.objects.filter(major='Marketing').count()
    stats = StudentInfo.objects.filter(major='Stats').count()
    
    context = {'freshman': freshman, 'sophomore': sophomore, 'junior': junior, 'senior': senior,
    'physics': physics, 'it': it, 'chemistry': chemistry, 'marketing': marketing, 'stats': stats}
    return render(request, "enrollment/home.html", context)

@login_required 
def studentdata(request):
    studentdata = StudentInfo.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data': pagedata}
    return render (request, "enrollment/studentinfo.html", context)

@login_required    
def coursedata(request):
    coursedata = CourseInfo.objects.all()
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data': pagedata}
    return render (request, "enrollment/courseinfo.html", context)

@login_required   
def enrollmentdata(request):
    studentdata = StudentInfo.objects.all()
    coursedata = CourseInfo.objects.all()
    enrollmentdata = EnrollmentInfo.objects.all()
    context = {'student':studentdata, 'course':coursedata, 'enrollment':enrollmentdata}
    return render(request, 'enrollment/enrollmentinfo.html', context)

@login_required
def saveinfo(request):
    if('student' in request.GET and 'course' in request.GET):
        studentdata = request.GET.get('student')
        coursedata = request.GET.get('course')        
        studentcount = EnrollmentInfo.objects.filter(studentname=studentdata).count()
        if(studentcount < 3):
            if not EnrollmentInfo.objects.filter(studentname=studentdata, coursename=coursedata).exists():
                data = EnrollmentInfo (studentname = studentdata, coursename=coursedata)
                data.save()
                return HttpResponse("Success")
        return HttpResponse("Error: Student cannot be enrolled in more than three classes")
        
        if(studentcount < 3):
            data = EnrollmentInfo (studentname = studentdata, coursename=coursedata)
            data.save()
            return HttpResponse("Success")
        return HttpResponse("Error")
        


