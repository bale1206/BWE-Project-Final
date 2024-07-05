from django import forms
from .models import CustomUser
from .models import User
from django.forms import ModelForm

class CustomUserCreationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'