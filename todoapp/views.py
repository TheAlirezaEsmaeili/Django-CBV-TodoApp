from django.shortcuts import render,redirect
from .models import TodoTask
from django.views.generic import ListView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class TodoListView(ListView):

    model = TodoTask
    template_name = 'todo/todotask.html'
    context_object_name = 'tasks'

    def post(self,request,*args,**kwargs):
        title = request.POST.get('title')
        if title:
            TodoTask.objects.create(title=title)
            return redirect('todoapp:todotask')

class TaskCreateView(CreateView):
    model = TodoTask
    fields = ["title"]
    success_url = reverse_lazy("todoapp:todotask")
    context_object_name = 'tasks'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskDeleteView(DeleteView):
    model = TodoTask
    template_name = 'todo/todotask_confirm_delete.html'
    success_url = reverse_lazy("todoapp:todotask")
    context_object_name = 'tasks'