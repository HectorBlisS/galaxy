from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from braces.views import LoginRequiredMixin
from .forms import CourseEnrollForm

# para dar acceso al contenido una vez enrollado
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from courses.models import Course




class StudentRegistrationView(CreateView):
	template_name = 'students/student/registration.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('students:student_course_list')

	def form_valid(self, form):
		result = super(StudentRegistrationView, self).form_valid(form)
		cd = form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password1'])
		login(self.request, user)
		return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
	course = None
	form_class = CourseEnrollForm

	def form_valid(self, form):
		self.course = form.cleaned_data['course']
		self.course.students.add(self.request.user)
		return super(StudentEnrollCourseView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('student_course_detail', args=[self.course.id])

# Mostramos al usuario los cursos que ha comprado

class StudentCourseListview(LoginRequiredMixin, ListView):
	model = Course
	template_name = 'students/course/list.html'

	def get_queryset(self):
		qs = super(StudentCourseListview, self).get_queryset()
		return qs.filter(students__in=[self.request.user])

class StudentCourseDetailView(DetailView):
	model = Course
	template_name = 'students/course/detail.html'

	def get_queryset(self):
		qs = super(StudentCourseDetailView, self).get_queryset()
		return qs.filter(students__in=[self.request.user])

	def get_context_data(self, **kwargs):
		context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
		# traer el curso
		course = self.get_object()
		if 'module_id' in self.kwargs:
			# traemos el modulo actual
			context['module'] = course.modules.get(id=self.kwargs['module_id'])
		else:
			# traemos el primer modulo
			context['module'] = course.modules.all()[0]
		return context


