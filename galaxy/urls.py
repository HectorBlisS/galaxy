from django.conf.urls import url, include
from django.contrib import admin
from main import urls as mainUrls
from courses import urls as coursesUrls
from accounts import urls as accountsUrls
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.views import password_reset, password_reset_confirm, password_reset_done, password_reset_complete
from students import urls as studentsUrls


urlpatterns = [
    
    url(r'^students/',
        include(studentsUrls, namespace="students")),

    url(r'^accounts/', 
        include(accountsUrls)),

    url(r'^admin/', admin.site.urls),

    url(r'^courses/',
        include(coursesUrls, namespace="courses")),

    url(r'^',
        include(mainUrls)),

    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),
]
