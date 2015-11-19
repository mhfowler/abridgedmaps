from django.conf.urls import patterns
from mhf.views import abridged_space, abridged_space2, abridged_space_take_me_anywhere, redirect
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
                       (r'^/$', abridged_space),
                       (r'^$', abridged_space),
                       (r'^gmaps/take_me_anywhere/$', abridged_space_take_me_anywhere),
                       (r'^gmaps2/$', abridged_space2),
                       (r'^/(?P<coordinates>.*)/$', abridged_space),
                       )

urlpatterns += patterns('',
                        (r'.*$',  redirect, {'page':"/"}),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


