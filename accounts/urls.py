from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, logout_then_login, login

urlpatterns = [
	url(r'^registration/', views.Registration.as_view(), name="registration"),
	url(r'^login/$', login, name="login"),
  url(r'^logout/$', logout, name="logout"),
  url(r'^logout-then-login/$', logout_then_login, name="logout_then_login"),
]