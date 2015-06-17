from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from content.views import movie_profile , suggested_films
from posts.views import post
from django.conf import settings
from django.conf.urls.static import static
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
    url(r'movies/(?:(?P<movie_id>\d+)/)?$', movie_profile),
    url(r'posts/(?:(?P<post_id>\d+)/)?$', post),
    url(r'^search/', temp_view),
    url(r'^test/', suggested_films),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
