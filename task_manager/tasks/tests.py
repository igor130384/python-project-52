from django.test import Client, TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='bon',
            first_name='Big',
            last_name='Bon',
            password='admin123456',
        )
        self.client.login(username='bon', password='admin123456')
        self.status = Status.objects.create(name='status_name')
        self.label = Label.objects.create(name='label_name')
        self.task = Task.objects.create(
            name='Task 1',
            description='Description of Task 1',
            status=self.status,
            author=self.user,
            executor=self.user
        )
        self.task_form_data = {
            'name': 'new name',
            'description': 'new description',
            'status': self.status.id,
            'labels': [self.label.id],
        }
        self.task.labels.add(self.label)

    def test_create_task_view(self):
        url = reverse('tasks_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_task_on_post(self):
        url = reverse('tasks_create')
        response = self.client.post(url, self.task_form_data)
        self.assertEqual(response.url, reverse('tasks_index'))

# Create your tests here.
