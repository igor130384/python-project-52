
from django.contrib.auth.forms import UserCreationForm

from .models import User


class NewUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password_text = 'Ваш пароль должен содержать как минимум 3 символа.'
        self.fields['password1'].help_text = password_text

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2')

#
# class UpdateForm(NewUserCreationForm):
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         return username
