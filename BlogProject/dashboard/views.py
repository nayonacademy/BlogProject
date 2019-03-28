from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bloglogin(request):
    return render(request, 'dashboard/login.html')

def showAllpost(request):
    return render(request, 'dashboard/allpost.html')

def updatePost(request, pk):
    return render(request, 'dashboard/addpost.html')

def newPost(request):
    return render(request, 'dashboard/addpost.html')

def settings(request):
    return HttpResponse("I am settings view")