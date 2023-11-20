from django.urls import path

from task_manager import views
from task_manager.statuses.views import IndexStatusView, StatusCreateView, StatusUpdateView, StatusDeleteView

urlpatterns = [
    path('', IndexStatusView.as_view(), name="tasks_index"),
    # path('create/', StatusCreateView.as_view(), name="status_create"),
    # path("<int:pk>/update/", StatusUpdateView.as_view(), name="status_update"),
    # path("<int:pk>/delete/", StatusDeleteView.as_view(), name="status_delete"),
]