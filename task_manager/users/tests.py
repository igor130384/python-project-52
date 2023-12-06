from django.test import Client, TestCase
from django.urls import reverse
from task_manager.users.forms import NewUserCreationForm
from task_manager.users.models import User


class UserCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.data = {
            'user1': {
                'username': 'bon',
                'first_name': 'Big',
                'last_name': 'Bon',
                'password1': 'admin123456',
                'password2': 'admin123456',
            }

        }

    def test_create_user_view(self):
        url = reverse('users_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user_form_valid(self):
        user = self.data['user1']
        form = NewUserCreationForm(user)
        self.assertTrue(form.is_valid())

    def test_create_user_on_post(self):
        url = reverse('users_create')
        user = self.data['user1']
        self.client.post(url, user)
        new_user = User.objects.last()
        self.assertEqual(user['username'], new_user.username)
        self.assertEqual(user['first_name'], new_user.first_name)
        self.assertEqual(user['last_name'], new_user.last_name)
