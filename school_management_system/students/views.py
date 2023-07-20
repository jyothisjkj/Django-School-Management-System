from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student_login(request):
    return render(request,"students/students_login.html")
    # return HttpResponse("thisis isis sisis")