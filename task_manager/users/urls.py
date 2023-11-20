from django.urls import path
from task_manager.users import views
from task_manager.users.views import UserUpdateView, UserDeleteView, UserCreateView

urlpatterns = [
    path('', views.IndexView.as_view(), name="users_index"),
    path('create/', UserCreateView.as_view(), name="users_create"),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
]