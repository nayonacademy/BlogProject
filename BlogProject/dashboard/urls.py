from django.urls import path
from . import views
urlpatterns = [
    path('login', views.bloglogin, name="login"),
    path('logout', views.bloglogout, name="logout"),
    path('', views.dashboard, name="dashboard"),
    path('posts', views.showAllpost, name='showallpost'),
    path('posts/<int:pk>', views.updatePost, name='updatePost'),
    path('posts/add', views.newPost, name='newpost'),
    path('settings', views.settings, name='settings')
]