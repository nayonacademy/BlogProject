from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('details/<int:pk>', views.postDetails, name="details"),
]