from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    description = models.CharField(_('Description'), max_length=255)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_('status'), related_name='status')
    author = models.ForeignKey(User, null=True, on_delete=models.PROTECT, related_name='author')
    executor = models.ForeignKey(User, blank=True,
                                 null=True, on_delete=models.PROTECT, related_name='executor',
                                 verbose_name=_('Executor'))
    labels = models.ManyToManyField(Label, blank=True, verbose_name=_('Labels'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
