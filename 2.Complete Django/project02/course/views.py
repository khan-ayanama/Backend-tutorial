from django.shortcuts import render
from django.http import HttpResponse


def learn_django(request):
    return render(request,'course/course.html')
