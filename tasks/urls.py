from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all', views.get_tasks, name='get_tasks'),
    path('post', views.post_task, name='post_task'),
]