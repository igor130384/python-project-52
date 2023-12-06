from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from task_manager.statuses import forms
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


# Create your views here.
class IndexStatusView(ListView):
    def get(self, request, *args, **kwargs):
        status = Status.objects.all()
        return render(request, 'statuses/status.html', {
            'status': status
        })


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        """Return a user creation form."""
        form = forms.StatusForm()
        return render(request, 'statuses/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """Create a new user."""
        form = forms.StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Status is successfully created'))
            return redirect('status_index')
        return render(request, 'statuses/create.html', {'form': form})


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'login'
    model = Status
    form_class = StatusForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy("status_index")
    success_message = _("Status successfully update")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("status_index")
    template_name = "statuses/delete.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _("Status is used by tasks"),
            )
        else:
            messages.success(
                self.request,
                _("Status successfully deleted"),
            )
        return HttpResponseRedirect(success_url)
