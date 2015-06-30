from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from content.views import movie_profile , suggested_films
from posts.views import timeline
from accounts.views import user_profile , follow_unfollow
from posts.views import post,post_comment, like
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^signup/', temp_view),
    url(r'users/(?:(?P<user_id>\d+)/)?$', user_profile),
    url(r'movies/(?:(?P<movie_id>\d+)/)?$', movie_profile),
    url(r'posts/(?:(?P<post_id>\d+)/)?$', post),
    url(r'^search/', temp_view),
    url(r'^test/', suggested_films),
    url(r'^$', timeline),
    url(r'^post-comment', post_comment),
    url(r'^like', like),
    url(r'^follow-unfollow', follow_unfollow),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
