from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, logout_then_login, login, password_reset, password_reset_confirm, password_reset_done, password_reset_complete

urlpatterns = [
	url(r'^registration/', views.Registration.as_view(), name="registration"),
	url(r'^login/$', login, name="login"),
  url(r'^logout/$', logout, name="logout"),
  url(r'^logout-then-login/$', logout_then_login, name="logout_then_login"),

  url(r'^password-reset/$',
    password_reset,
    name="password_reset"),
  url(r'^password-reset/done/$',
    password_reset_done,
    name='password_reset_done'),
  url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    password_reset_confirm,
    name="password_reset_confirm"),
  url(r'^password-reset/complete/$',
    password_reset_complete,
    name='password_reset_complete'),

]