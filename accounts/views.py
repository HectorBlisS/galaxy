from django.shortcuts import render
from django.views.generic import View

from .forms import UserRegistrationForm

class Registration(View):
	def get(self, request):
		template_name = 'accounts/registration.html'
		form = UserRegistrationForm()