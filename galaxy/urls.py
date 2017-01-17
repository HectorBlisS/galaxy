from django.conf.urls import url, include
from django.contrib import admin
from main import urls as mainUrls
from courses import urls as coursesUrls
from accounts import urls as accountsUrls
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^courses/',
    	include(coursesUrls)),

    url(r'^',
    	include(mainUrls)),

    url(r'^accounts/', 
        include(accountsUrls, namespace="accounts")),

    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),

]
