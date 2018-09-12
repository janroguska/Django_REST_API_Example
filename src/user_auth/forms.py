from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

"""Handles user creation and change forms
"""
class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'name')

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields