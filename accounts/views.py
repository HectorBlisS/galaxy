from django.shortcuts import render, redirect
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, ProfileForm

from .models import Profile

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = 'accounts/dashboard.html'
		form = ProfileForm()
		context = {
			'form':form
		}
		return render(request, template_name, context)

class Registration(View):
	def get(self, request):
		template_name = 'registration/registration.html'
		form = UserRegistrationForm()

		context = {
			'form':form
		}

		return render(request, template_name, context)

	def post(self, request):

		new_user_form = UserRegistrationForm(request.POST)

		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()

			profile = Profile()
			profile.user = new_user
			profile.save()

			return redirect('accounts:profile')

		else:
			template_name = 'registration/registration.html'
			context = {
				'form':UserRegistrationForm(),
			}
			return render(request, template_name)