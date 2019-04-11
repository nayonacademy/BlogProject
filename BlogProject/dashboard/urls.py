from django.urls import path
from . import views
urlpatterns = [
    path('login', views.bloglogin, name="login"),
    path('logout', views.bloglogout, name="logout"),
    path('', views.dashboard, name="dashboard"),
    path('posts', views.showAllpost, name='showallpost'),
    path('category', views.category, name='category'),
    path('category_status/<int:pk>', views.category_status, name='category_status'),
    path('category_update/<int:pk>',views.category_update,name='category_update'),
    path('posts/<int:pk>', views.updatePost, name='updatePost'),
    path('posts/delete/<int:pk>', views.postdelete, name='postdelete'),
    path('category/delete/<int:pk>', views.category_delete, name='category_delete'),
    path('category/edit/<int:pk>', views.category_edit, name='category_edit'),
    path('posts/add', views.newPost, name='newpost'),
    path('posts/update/<int:pk>', views.postupdate, name='postupdate'),
    path('settings', views.settings, name='settings')
]