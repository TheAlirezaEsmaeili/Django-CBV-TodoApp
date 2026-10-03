from django.urls import path,include
from .views import TodoListView,TaskCreateView,TaskDeleteView
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('',views.TodoListView.as_view(),name='todotask'),
    path('create',views.TaskCreateView.as_view(),name='task_create'),
    path('delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete')

]