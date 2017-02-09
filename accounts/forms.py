from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Ingresa tu contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma tu contraseña', widget=forms.PasswordInput)

	class Meta():
		model = User
		fields = ('username', 'first_name', 'email', )

	def cleaned_password(self):
		cd = self.cleaned_data

		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta():
		model = User
		fields = ('username', 'first_name', 'email', )

class ProfileForm(forms.ModelForm):
	cover = forms.ImageField(label='Foto de portada', widget=forms.FileInput(attrs={'class':'imageprofile', 'required':'false'}))
	avatar = forms.ImageField(label='Foto de perfil', widget=forms.FileInput(attrs={'class':'imageprofile', 'required':'false'}))
	class Meta():
		model = Profile
		fields = ('cover', 'avatar', 'birth', 'tel', 'bio')
