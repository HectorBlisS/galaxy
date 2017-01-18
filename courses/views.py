from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Course, Module, Content

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin


class OwnerMixin(object):
	def get_queryset(self):
		qs = super(OwnerMixin, self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(OwnerEditMixin, self).form_valid(form)

class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin):
	model = Course

class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
	fields = ['subject', 'title', 'slug', 'overview']
	success_url = reverse_lazy('manage_course_list')
	template_name = 'courses/manage/course/form.html'


class ManageCourseListView(OwnerCourseMixin, ListView):
	template_name = 'courses/manage/course/list.html'

class CourseCreateView(PermissionRequiredMixin, OwnerCourseEditMixin, CreateView):
	permission_required = 'courses.add_course'

class CourseUpdateView(PermissionRequiredMixin, OwnerCourseEditMixin, UpdateView):
	permission_required = 'courses.change_course'

class CourseDeleteView(PermissionRequiredMixin, OwnerCourseMixin, DeleteView):
	template_name = 'courses/manage/course/delete.html'
	success_url = reverse_lazy('manage_course_list')
	permission_required = 'courses.delete_course'

# class ManageCourseListView(ListView):
# 	model = Course
# 	template_name = 'courses/manage/course/list.html'

# 	def get_queryset(self):
# 		qs = super(ManageCourseListView, self).get_queryset()
# 		return qs.filter(owner=self.request.user)

# List and Detail View
class CourseListView(ListView):
	model = Course
	template_name = 'courses/list.html'

class CourseDetailView(View):
	def get(self, request, slug):
		template_name = 'courses/detail.html'
		course = Course.objects.get(slug = slug)
		modules = Module.objects.filter(course = course)
		print(modules)
		context = {'course':course,'modules':modules}
		return render(request,template_name,context)