from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^mine/$',
		views.ManageCourseListView.as_view(),
		name="manage_course_list"),

	url(r'^create/$',
		views.CourseCreateView.as_view(),
		name="course_create"),

	url(r'^(?P<pk>\d+)/edit/$',
		views.CourseUpdateView.as_view(),
		name="course_edit"),

	url(r'^(?P<pk>\d+)/delete/$',
		views.CourseDeleteView.as_view(),
		name="course_delete"),

	# Para el formset
	url(r'^(?P<pk>\d+)/module/$',
		views.CourseModuleUpdateView.as_view(),
		name="course_module_update"),

	# url for content
	url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
		views.ContentCreateUpdateView.as_view(),
		name="module_content_create"),

	url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$',
		views.ContentCreateUpdateView.as_view(),
		name="module_content_update"),

	# delete content
	url(r'^content/(?P<id>\d+)/delete/$',
		views.ContentDeleteView.as_view(),
		name="module_content_delete"),

	# crm content
	url(r'^module/(?P<module_id>\d+)/$',
		views.ModuleContentListView.as_view(),
		name="module_content_list"),

	# Reordenar modulos y contenidos
	url(r'^module/order/$',
		views.ModuleOrderView.as_view(),
		name="module_order"),

	url(r'^content/order/$',
		views.ContentOrderView.as_view(),
		name="content_order"),

#list and detail views

	url(r'^(?P<slug>[\w-]+)$',
		views.CourseDetailView.as_view(),
		name="course_detail"),

	url(r'^$',
		views.Subjects.as_view(),
		name="subject_list"),

	#
#subjects
	url(r'^subjects/(?P<slug>[\w-]+)$', views.SubjectDetail.as_view(), name="subject_detail"),
    url(r'^subjects/(?P<slug>[\w-]+)/(?P<course_slug>[\w-]+)$', views.SubjectDetail.as_view(), name="subject_detail_with_course"),

]