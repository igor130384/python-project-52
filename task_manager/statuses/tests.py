from django.test import Client, TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User


class StatusCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='bon',
            first_name='Big',
            last_name='Bon',
            password='admin123456',
        )
        self.client.login(username='bon', password='admin123456')
        self.status = Status.objects.create(
            name='name',
            created_at='2022-01-01T00:00:00Z'
        )

    def test_create_status_view(self):
        url = reverse('status_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        new_form_data = {
            'name': 'new_name',
        }
        response = self.client.post(url, new_form_data)
        self.assertEqual(response.status_code, 302)

    def test_create_status_on_post(self):
        url = reverse('status_create')
        form_data = {'name': 'old_name', }
        response = self.client.post(url, form_data)
        self.assertEqual(response.url, reverse('status_index'))


# Create your tests here.
