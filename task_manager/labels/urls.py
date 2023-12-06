from django.urls import path

from task_manager.labels.views import IndexLabelsView, LabelsUpdateView, \
    LabelsCreateView, LabelsDeleteView

urlpatterns = [
    path('', IndexLabelsView.as_view(), name="label_index"),
    path('create/', LabelsCreateView.as_view(), name="labels_create"),
    path("<int:pk>/update/", LabelsUpdateView.as_view(), name="labels_update"),
    path("<int:pk>/delete/", LabelsDeleteView.as_view(), name="labels_delete"),
]
