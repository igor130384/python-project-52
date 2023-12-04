import django_filters
from django import forms
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import User


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        field_name="creator",
        method="get_self_tasks",
        label=_("Only own tasks"),
        widget=forms.CheckboxInput(),
    )
    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        queryset=Status.objects.all(),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Executor'),
        queryset=User.objects.all(),
    )
    label = django_filters.ModelChoiceFilter(
        field_name="labels",
        label=_("Label"),
        queryset=Label.objects.all(),
    )

    def get_self_tasks(self, queryset, name, value):
        if value is not None:
            return queryset
        return queryset.filter(creator=self.request.user)

    class Meta:
        model = Task
        fields = ["status", "executor", "label"]
