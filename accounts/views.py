from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, ProfileForm, UserEditForm

from .models import Profile

from braces.views import LoginRequiredMixin
from django.views.generic.base import TemplateResponseMixin
from django.contrib.auth.models import User

# follow users
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# from common.decorators import ajax_required
from .models import Contact

# Activity stream actions
from actions.utils import create_action
from actions.models import Action



# <- Listado de usuarios para seguirlos
class UserList(LoginRequiredMixin, TemplateResponseMixin, View):
	template_name = "accounts/user/list.html"
	def get(self, request):
		users = User.objects.filter(is_active=True)
		return self.render_to_response({'section':'people','users':users})

class UserDetail(LoginRequiredMixin, TemplateResponseMixin, View):
	template_name="accounts/user/detail.html"
	def get(self, request, username):
		user = get_object_or_404(User, username=username, is_active=True)
		return self.render_to_response({'section':'people','user':user})
# Listado de usuarios para seguirlos ->

# Seguir y dejar de seguir usuarios
@require_POST
@login_required
def user_follow(request):
	if request.is_ajax():
		user_id = request.POST.get('id')
		action = request.POST.get('action')
		if user_id and action:
			try:
				user = User.objects.get(id=user_id)
				if action == 'follow':
					Contact.objects.get_or_create(
						user_from=request.user,
						user_to=user)
					create_action(request.user, 'está siguiendo a', user)
				else:
					Contact.objects.filter(user_from=request.user,
						user_to=user).delete()
				return JsonResponse({'status':'ok'})
			except User.DoesNotExist:
				return JsonResponse({'status':'ko'})
	return JsonResponse({'status':'ko'})




class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		#mostramos todas las acciones por default
		actions = Action.objects.exclude(user=request.user)
		following_ids = request.user.following.values_list('id',flat=True)
		if following_ids:
			# si el usuario está siguiendo a otros, filtramos las acciones
			# actions = actions.filter(user_id__in=following_ids)
			# optimizando la peticion:
			actions = actions.filter(user_id__in=following_ids).select_related('user','user__profile').prefetch_related('target')
		actions = actions[:10]

		template_name = 'accounts/dashboard.html'
		form_profile = ProfileForm(instance=request.user.profile)
		form_user_edit = UserEditForm(instance=request.user)
		context = {
			'form_profile':form_profile,
			'actions':actions,
			'form_user':form_user_edit
		}
		return render(request, template_name, context)

	def post(self, request):
		pass


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

			return redirect('dashboard')

		else:
			template_name = 'registration/registration.html'
			context = {
				'form':UserRegistrationForm(),
			}
			return render(request, template_name)