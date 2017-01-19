from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^registration/', views.Registration.as_view(), name="registration"),
	url(r'^login/$', auth_views.login, name="login"),
  url(r'^logout/$', auth_views.logout, name="logout"),
  url(r'^logout-then-login/$', auth_views.logout_then_login, name="logout_then_login"),

  url(r'^profile/', views.Dashboard.as_view(), name="dashboard"),

  url(r'^password-reset/$',
    auth_views.password_reset,
    {'template_name':'registration/password_reset_form.html',
    'email_template_name':'registration/password_reset_email.html',
    'html_email_template_name':'registration/password_reset_email.html'},
    name="password_reset"),

  url(r'^password-reset/done/$',
    auth_views.password_reset_done,
    name='password_reset_done'),

  url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    auth_views.password_reset_confirm,
    name="password_reset_confirm"),

  url(r'^password-reset/complete/$',
    auth_views.password_reset_complete,
    name='password_reset_complete'),

]