import django_filters
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import User


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        field_name="author",
        label_suffix="",
        method="get_self_tasks",
        label=_("Only own tasks"),
        widget=CheckboxInput(),
    )
    status = django_filters.ModelChoiceFilter(
        label=_('status'),
        label_suffix="",
        queryset=Status.objects.order_by('name'),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Executor'),
        label_suffix="",
        queryset=User.objects.order_by('first_name', 'last_name'),
    )
    label = django_filters.ModelChoiceFilter(
        field_name="labels",
        label=_("Label"),
        label_suffix="",
        queryset=Label.objects.all(),
    )

    def get_self_tasks(self, queryset, name, value):
        return queryset.filter(author=self.request.user.pk) if value else queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "label"]
