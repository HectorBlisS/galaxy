from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Ingresa tu contraseña', widget=forms.PasswordInput)
	password = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput)

	class Meta():
		model = User
		fields = ('username', 'first_name', 'email')

	def cleaned_password(self):
		cd = self.cleaned_data

		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['password2']
