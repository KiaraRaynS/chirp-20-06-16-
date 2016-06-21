from django.conf.urls import url, include
from django.contrib import admin
from appdjango.views import ViewIndex, ChirpDetailView, CreateChirp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewIndex.as_view(), name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^chirpdata/(?P<pk>\d+)/$', ChirpDetailView.as_view(), name='detailview'),
    url(r'^createchirp/$', CreateChirp.as_view(), name='chirpcreate')
]
