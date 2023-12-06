from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView

from . import forms
from .forms import NewUserCreationForm
from .mixin import UserHasPermissionMixin
from .models import User


# Create your views here.
class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/users.html', {
            'users': users
        })


class UserCreateView(View):
    """User create page view."""

    def get(self, request, *args, **kwargs):
        """Return a user creation form."""
        form = forms.NewUserCreationForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        """Create a new user."""
        form = forms.NewUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('User is successfully created'))
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserUpdateView(UserHasPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = NewUserCreationForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users_index")
    success_message = _("User successfully updated")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserDeleteView(UserHasPermissionMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users_index")
    template_name = "users/delete.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _("Cannot delete a user because he is being used"),
            )
        else:
            messages.success(
                self.request,
                _("User successfully deleted"),
            )
        return HttpResponseRedirect(success_url)
