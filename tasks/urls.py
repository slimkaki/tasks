from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all', views.getTasks, name='getTasks')
    path('post', views.postTask, name='postTask')
]