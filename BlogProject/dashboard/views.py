from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.

def bloglogin(request):
    if request.method == 'GET':
        return render(request, 'dashboard/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return HttpResponseRedirect(reverse('login'))

@login_required
def bloglogout(request):
    logout(request)
    context = {
        'message': 'Successfully Logout'
    }
    return render(request,'dashboard/login.html',context)

@login_required
def showAllpost(request):
    return render(request, 'dashboard/post_list.html')

@login_required
def updatePost(request, pk):
    return render(request, 'dashboard/update_post.html')

@login_required
def newPost(request):
    return render(request, 'dashboard/create_post.html')

@login_required
def settings(request):
    return HttpResponse("I am settings view")

@login_required
def dashboard(request):
    return render(request, 'dashboard/admin_home.html')