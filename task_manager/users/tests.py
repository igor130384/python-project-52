from django.test import Client, TestCase

from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

from task_manager.users.forms import NewUserCreationForm
from task_manager.users.models import User


class UserCreateTest(TestCase):
    """Test user creation operations."""

    def setUp(self):
        """Set initial condition for each test method."""
        self.client = Client()
        self.data = {
            'user1': {
                'username': 'tota',
                'first_name': 'Tota',
                'last_name': 'Totavich',
                'password1': 'adminadmin',
                'password2': 'adminadmin',
            },
            'user2': {
                'username': 'dada',
                'first_name': 'Dada',
                'last_name': 'Dadavich',
                'password1': 'adminadmin',
                'password2': 'adminadmin',
            }

        }

    def test_create_user_view(self):
        """Test user creation view."""
        url = reverse('users_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

#     def test_create_user_form_valid(self):
#         """Test user creation form validation with correct data."""
#         user = self.data['user1']
#         form = NewUserCreationForm(user)
#         self.assertTrue(form.is_valid())
#
#     def test_create_user_on_post(self):
#         """Test user creation on post."""
#         url = reverse('users_create')
#         user = self.data['user1']
#         self.client.post(url, user)
#         new_user = User.objects.last()
#         self.assertEqual(user['username'], new_user.username)
#         self.assertEqual(user['first_name'], new_user.first_name)
#         self.assertEqual(user['last_name'], new_user.last_name)
#
#
# class UserRUDTest(TestCase):
#     """Test user read, update, delete operations."""
#
#     def setUp(self):
#         """Set initial condition for each test method."""
#         self.client = Client()
#         self.test_user = User.objects.create_user(
#             username='test_user',
#             password='123',
#         )
#
#         self.data = {
#             'user': {
#                 'username': 'tota',
#                 'first_name': 'Tota',
#                 'last_name': 'Totavich',
#                 'password': 'adminadmin',
#             }
#         }
#
#     def test_update_user(self):
#         """Test user update data."""
#         self.users_update_url = reverse(
#             'users_update',
#             args=[self.test_user.pk],
#         )
#         self.client.login(
#             username="test_user",
#             password="123",
#         )
#         response1 = self.client.post(
#             self.users_update_url,
#             {
#                 'first_name': 'test_user',
#                 'username': 'test_user',
#                 'password1': 't',
#                 'password2': 't',
#             }
#         )
#         self.assertEquals(response1.status_code, 200)
#         self.assertTemplateUsed(response1, 'users/update.html')
#
#     def test_delete_user(self):
#         """Test user delete."""
#         user_data = self.data['user']
#         user = User.objects.create_user(**user_data)
#
#         login_url = reverse('login')
#         self.client.post(
#             login_url, {
#                 'username': user_data['username'],
#                 'password': user_data['password']
#             }
#         )
#         url = reverse('users_delete', kwargs={'pk': user.pk})
#         self.client.post(url)
#         with self.assertRaises(ObjectDoesNotExist):
#             User.objects.get(pk=user.pk)
