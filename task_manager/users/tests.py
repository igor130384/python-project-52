from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .models import User


# Create your tests here.

class UserTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(first_name='igor', last_name='gorshkov', username='giv84')
        self.assertEqual(user.username, 'giv84')
        self.assertEqual(str(user.first_name + ' ' + user.last_name), 'igor gorshkov')
        self.assertTrue(isinstance(user, User))

    def test_edite_user(self):
        response = self.client.post(
            reverse('users_create'),
            {'first_name': 'Katy', 'last_name': 'Perry',
             'username': 'katy_perry', 'password1': 'kBPfn673ls',
             'password2': 'kBPfn673ls'}
        )
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('login'))

        # messages = list(get_messages(response.wsgi_request))
        # self.assertEqual(str(messages[0]),
        #                  'Пользователь успешно зарегистрирован')
