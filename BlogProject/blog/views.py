from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import *
# Create your views here.

def index(request):
    allpost = BlogPost.objects.all()
    context = {
        'allpost' : allpost
    }
    return render(request, 'blog/home.html',context)

def postDetails(request, pk):
    details_post = BlogPost.objects.filter(id=pk)
    context = {
        'details_post': details_post
    }
    return render(request, 'blog/post_details.html',context)