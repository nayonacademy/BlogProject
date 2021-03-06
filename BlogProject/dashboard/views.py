from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms.category import *
from .forms.post import *

# Create your views here.

def bloglogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome Back')
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            messages.warning(request, 'Invalid Credentials')
            return HttpResponseRedirect(reverse('login'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        return render(request, 'dashboard/login.html')


@login_required
def bloglogout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return HttpResponseRedirect(reverse('login'))


@login_required
def showAllpost(request):
    all_post = BlogPost.objects.all()
    context = {
        'all_post': all_post
    }
    return render(request, 'dashboard/post_list.html', context)


@login_required
def updatePost(request, pk):
    post=get_object_or_404(BlogPost,pk)
    if request.method == "GET":
        form=BlogPostForm(instance=post)
        context={
        'form': form
        }
        return render(request, 'dashboard/update_post.html')

    
@login_required
def newPost(request):
    if request.method == "GET":
        form =BlogPostForm()
        allcategory = Category.objects.filter(category_status='Active')
        context = {
            'category_list': allcategory,
            'form': form
        }
        return render(request, 'dashboard/create_post.html',context)

    if request.method == "POST":
        form = BlogPostForm(request.POST)
        print(form)
        form.save()
 
        # title = request.POST.get('post_title', None)
        # desc = request.POST.get("post_des", None)
        # category_name = request.POST.get("category_name", None)
        # print(title, desc,category_name)
        # BlogPost.objects.create(title=title, details=desc, category_id=category_name)
        # messages.success(request, 'Successfully Add new post')
        return HttpResponseRedirect(reverse('showallpost'))


@login_required
def postdelete(request, pk):
    BlogPost.objects.filter(pk=pk).delete()
    messages.info(request, 'Delete post')
    return HttpResponseRedirect(reverse('showallpost'))


@login_required
def postupdate(request, pk):
    post=get_object_or_404(BlogPost,pk=pk)
    if request.method == "GET":
        form=BlogPostForm(instance=post)
        context={
        'form': form
        }
        return render(request, 'dashboard/update_post.html',context)
    elif request.method == "POST":
        form=BlogPostForm(request.POST,instance=post)
        if form.is_valid():
            post.save()
            messages.info(request,'postupdate Successfully !')
            return HttpResponseRedirect(reverse('showallpost'))
        else:
            messages.info(request,'this post will not updatePost.')
            return HttpResponseRedirect(reverse('showallpost'))

@login_required
def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
#         # category_name = request.POST.get('category_name', None)
#         # category_description = request.POST.get('category_description', None)
#         # category_status = request.POST.get('category_status', None)
#         # Category.objects.create(category_name=category_name, category_description=category_description,
#         # category_status=category_status)
        return HttpResponseRedirect(reverse('category'))
    else:
        form = CategoryForm()
        category_data = Category.objects.all()
        context = {
            'category_data': category_data,
            'form' : form
        }
        return render(request, 'dashboard/create_category.html', context)

<<<<<<< HEAD
def category_update(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category'))
    if request.method == 'GET':
        form=CategoryForm(instance=category)
    context={
            'form':form
          }

    return render(request,'dashboard/category_edit.html',context)    
=======
# def category_update(request,pk):
#     if request.method == 'POST':
       
#         category_data=get_object_or_404(Category,pk=pk)
#         form=CategoryForm(request.POST,instance=category_data)
#         form.save()
#         return HttpResponseRedirect(reverse('category'))
#     if request.method == 'GET':
#         category=get_object_or_404(Category,pk=pk)
#         form=CategoryForm(request.POST or None,instance=category)
#         # print(form)
#         context={
#             'form':form
#         }

#         return render(request,'dashboard/category_edit.html',context)    
@login_required
def category_edit(request,pk):
    data=get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Category Updated Successfully')
            return HttpResponseRedirect(reverse('category'))
    else:        
        form=CategoryForm(instance=data)
    context={
        'form':form
    }
    return render(request, 'dashboard/edit_category.html',context) 

>>>>>>> master
@login_required
def category_delete(request, pk):
    category = Category.objects.filter(pk=pk).delete()
    messages.info(request, 'Category Deleted !')
    return HttpResponseRedirect(reverse('category'))


@login_required
def category_status(request, pk):
    category_data = get_object_or_404(Category, pk=pk)
    if category_data.category_status == 'Active':
        category_data.category_status = 'Inactive'
        messages.info(request, 'Category Status Changed Into Inactive !')
    else:
        category_data.category_status = 'Active'
        messages.success(request, 'Category Status Changed Into Active !')
    category_data.save()
    return HttpResponseRedirect(reverse('category'))


@login_required
def settings(request):
    return HttpResponse("I am settings view")


@login_required
def dashboard(request):
    return render(request, 'dashboard/admin_home.html')

