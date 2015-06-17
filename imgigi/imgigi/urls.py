from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from accounts.views import signup
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def temp_view(request, user_id):
    id = user_id
    return HttpResponse("id = " + id)


urlpatterns = [
    # Examples:
    # url(r'^$', 'imgigi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', temp_view),
    url(r'^forgot-pass/', temp_view),
    url(r'^signup/$', signup),
    url(r'^$/', temp_view),
    url(r'users/(?:(?P<user_id>\d+)/)?$', temp_view),
    url(r'movies/(?:(?P<movie_id>\d+)/)?$', temp_view),
    url(r'posts/(?:(?P<post_id>\d+)/)?$', temp_view),
    url(r'^search/', temp_view),
]

urlpatterns += staticfiles_urlpatterns()