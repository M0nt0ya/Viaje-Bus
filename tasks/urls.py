from django.urls import path
from . import views

urlpatterns = [
  path('', views.list_tasks),
  path('new/', views.create_task, name='create_task'),
  path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
  path('update', views.update, name='update'),
  path('update/<int:task_id>/', views.update_from, name='update_from'),
 ]