from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from marksheet.models import Marksheet

def sheet(request):
    marksData=Marksheet.objects.all()
    marks_with_sums = []
    
    for obj in marksData:
        total = (obj.subject1 + obj.subject2 + obj.subject3 + obj.subject4 + obj.subject5 + obj.subject6)
        percentage=round((total/600)*100,2)
        if percentage>85:
            grade="A"
        elif percentage>65:
            grade="B"
        elif percentage>50:
            grade="C"
        else:
            grade="F"
        
        marks_with_sums.append({
            'obj': obj,
            'total': total,
            'percentage': percentage,
            'grade': grade,
        })
    
    data = {
        'students': marks_with_sums,
        'max': 600,
    }
    # data={
    #     'marksData':marksData,
    #     'max':600,
    #     }
    return render (request,"marksheet.html",data)


def task(request):
    return render(request,"index2.html")

def home(request):
    data={
        'title': 'Home Page',
        'name': 'Syed Ashhal Abbas Zaidi',
        'clist': ['Ahmed' ,'Muneeb', 'Daniyal'],
        'numbers': [10,20,30,40,50,60,70,80],
         #'numbers': [],
        'students': [
            {'name':'Ashhal','age':432},
            {'name':'Muneed','age':75},
            {'name':'Ahmed','age':3532},
        ]
    }
    return render(request,"home.html",data)

def ashhalAbbas(request):
    return HttpResponse("<h1 style='color : red;'>Welcome to my first page in django, my name is Syed Ashhal Abbas Zaidi</h1>")

def course(request):
    return HttpResponse("These are the courses")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def userForm(request):
    res=0
    data={}
    try:
        if request.method=="POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            res=n1+n2
            data = {'n1':n1,'n2':n2,'output':res}

            url = "/task/?output={}".format(res)

            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"userform.html",data)

def about(request):
    return HttpResponse("About U spage")