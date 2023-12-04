from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.utils.translation import gettext as _
from django_filters.views import FilterView

from .filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class IndexTaskView(ListView, FilterView):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        tasks_filtered = TaskFilter(request.GET, queryset=tasks)
        return render(request, 'tasks/task.html', {'filter': tasks_filtered})


class TasksCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks_index")
    success_message = _("Task successfully created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = 'task'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks_index")
    template_name = "tasks/delete.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _("Only its author can delete a task"),
            )
        else:
            messages.success(
                self.request,
                _("Task successfully deleted"),
            )
        return HttpResponseRedirect(success_url)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Task
    form_class = TaskForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks_index")
    success_message = _("Task successfully update")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# Create your views here.
