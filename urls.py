from django.conf.urls import patterns, include, url
from mhf.views import viewWrapper, home, redirect, machine_learning, twitter_visualization,map_reduce, \
    loadingCrazy, theHome, submitEmail, monkeySkull, brocasCoconut, capitalistTees, buyShirt, \
    writing, art, contact, about, truespeak, truespeakPublicDetail, truespeakSecretLink, publishTexts, \
    projects, store, vr_landing, abridged_space, abridged_space2, abridged_space_take_me_anywhere
from bots.trashbot import trashBot, check_for_dms_endpoint
from settings.common import LOCAL, STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

# urlpatterns = patterns('',
#     # ... the rest of your URLconf goes here ...
# ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#
# patterns for mhfowler
urlpatterns = patterns('',
                       (r'^/$', viewWrapper(abridged_space)),
                       (r'^gmaps/take_me_anywhere/$', viewWrapper(abridged_space_take_me_anywhere)),
                       (r'^gmaps2/$', viewWrapper(abridged_space2)),
                       (r'^/(?P<coordinates>.*)/$', viewWrapper(abridged_space)),
                       )

# # # redirect everything else
urlpatterns += patterns('',
                        (r'^/$',  redirect, {'page':"/"}),
                        (r'^$',  redirect, {'page':"/"}),
                        # (r'.*$',  redirect, {'page':"/home/"}),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


