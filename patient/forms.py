from django.forms import ModelForm
from .models import PatientInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateForm(ModelForm):
    class Meta:
        model = PatientInfo
        fields = ['name', 'email', 'phone', 'age', 'address']



