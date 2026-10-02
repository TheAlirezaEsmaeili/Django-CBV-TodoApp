from django.shortcuts import render,redirect
from .models import TodoTask
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class todoListView(ListView):

    model = TodoTask
    template_name = 'todo/todotask.html'
    context_object_name = 'tasks'

    def post(self,request,*args,**kwargs):
        title = request.POST.get('title')
        if title:
            TodoTask.objects.create(title=title)
            return redirect('todotask')

class TaskCreate(CreateView):
    model = TodoTask
    fields = ["title"]
    success_url = reverse_lazy("todotask")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
