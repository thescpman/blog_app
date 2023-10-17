"""Defines url patterns for learning_logs"""

from django.urls import path

from . import views


app_name = 'blog_app'

urlpatterns = [
    #Home Pgae
    path('', views.index, name='index'),
    path('blogs/', views.blogs,name='blogs'),
    path('new_blog/',views.newblog,name='newblog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]