from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_all', views.get_all_tasks, name='get_all_tasks'),
    path('get_single/<int:id_task>', views.get_single_task , name='get_single_task'),
    path('post', views.post_task, name='post_task'),
    path('delete/<int:id_task>', views.delete_task , name='delete_task'),
    path('update/<int:id_task>', views.update_task , name='update_task'),
]