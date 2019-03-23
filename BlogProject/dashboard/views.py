from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bloglogin(request):
    return HttpResponse("I am login page")

def showAllpost(request):
    return HttpResponse("Show all post in a table")

def updatePost(request, pk):
    return HttpResponse("I am update post view")

def newPost(request):
    return HttpResponse("I am add new post")

def settings(request):
    return HttpResponse("I am settings view")