from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label


class IndexLabelsView(ListView):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request, 'labels/label.html', {
            'labels': labels
        })


class LabelsCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = "labels/create.html"
    success_url = reverse_lazy("label_index")
    success_message = _("Labels successfully created")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        return super().form_valid(form)


class LabelsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Label
    form_class = LabelForm
    template_name = "labels/update.html"
    success_url = reverse_lazy("label_index")
    success_message = _("Labels successfully update")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LabelsDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    success_url = reverse_lazy("label_index")
    template_name = "labels/delete.html"
    success_message = _("Labels successfully deleted")
# Create your views here.
