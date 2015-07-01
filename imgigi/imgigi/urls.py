from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.http import HttpResponse
from content.views import movie_profile , suggested_films, search
from posts.views import post,post_comment, like , red_notifications
from posts.views import post, timeline, add_post
from django.conf import settings
from django.conf.urls.static import static
import notifications
from accounts.views import follow_unfollow, user_profile, signup, login, edit_user_profile
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def temp_view(request, user_id):
    id = user_id
    return HttpResponse("id = " + id)


urlpatterns = [
    # Examples:
    # url(r'^$', 'imgigi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^signup/$', signup),
    url('^change-password/', auth_views.password_change),
    url(r'^password_change/done/$', edit_user_profile, name='password_change_done'),
    url('^logout/', auth_views.logout_then_login),
    url(r'^edit-profile/$', edit_user_profile),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'users/(?:(?P<user_id>\d+)/)?$', user_profile),
    url(r'movies/(?:(?P<movie_id>\d+)/)?$', movie_profile),
    url(r'posts/(?:(?P<post_id>\d+)/)?$', post),
    url(r'^search/', search),
    url(r'^$', timeline),
    url(r'^timeline/(?P<page_index>\d+)/$', timeline),
    url(r'^post-comment', post_comment),
    url(r'^like', like),
    url(r'^follow-unfollow', follow_unfollow),
    #url(r'^edit', edit),
    url('^notifications/', include(notifications.urls)),
    url('^read-notifications/', red_notifications),
    url('^add-post/', add_post),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)