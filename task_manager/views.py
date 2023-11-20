from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    success_message = _("You are logged in")
    next_page = reverse_lazy('index')
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("index")


class LogoutUser(LogoutView):
    next_page = reverse_lazy("index")
    success_message = _('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, _("You are logged out"))
        return response
