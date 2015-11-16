from django.conf.urls import patterns, include, url
from mhf.views import viewWrapper, home, redirect, machine_learning, twitter_visualization,map_reduce, \
    loadingCrazy, theHome, submitEmail, monkeySkull, brocasCoconut, capitalistTees, buyShirt, \
    writing, art, contact, about, truespeak, truespeakPublicDetail, truespeakSecretLink, publishTexts, \
    projects, store, vr_landing, abridged_space, abridged_space2
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
                       # (r'^$', viewWrapper(monkeyLoader)),
                       (r'^______/$', viewWrapper(theHome)),
                       (r'^~/$', viewWrapper(monkeySkull)),
                       (r'^brocascoconut/$', viewWrapper(brocasCoconut)),
                       (r'^LOADING/(?P<page>\w+)/$', viewWrapper(loadingCrazy)),

                       # posts
                       (r'^submit_email/$', viewWrapper(submitEmail)),

                       # capitalist products
                       (r'^the_capitalist_tshirt/$', viewWrapper(capitalistTees)),
                       (r'^the_capitalist_print/$', viewWrapper(capitalistTees)),
                       (r'^the_capitalist_booty/$', viewWrapper(capitalistTees)),

                       # other pages
                       (r'^gmaps/$', viewWrapper(abridged_space)),
                       (r'^gmaps2/$', viewWrapper(abridged_space2)),
                       (r'^gmaps/(?P<coordinates>.*)/$', viewWrapper(abridged_space)),
                       (r'^writing/$', viewWrapper(writing)),
                       (r'^art/$', viewWrapper(art)),
                        (r'^vr/$', viewWrapper(vr_landing)),
                       (r'^projects/$', viewWrapper(projects)),
                       (r'^store/$', viewWrapper(store)),
                       (r'^contact/$', viewWrapper(contact)),
                       (r'^about_brocas/$', viewWrapper(about)),
                       (r'^buyShirt/$', viewWrapper(buyShirt)),

                       # actions
                       (r'^trashbot/$', viewWrapper(trashBot)),
                       (r'^check_for_dms/$', viewWrapper(check_for_dms_endpoint)),

                       # truespeak
                       (r'^truespeak/$', viewWrapper(truespeak)),
                       (r'^truespeak/(?P<name>\w+)/(?P<appendage>\d+)/$', viewWrapper(truespeakPublicDetail)),
                       (r'^secretlink/(?P<name>\S+)/(?P<appendage>\d+)/$', viewWrapper(truespeakSecretLink)),
                       (r'^publish_texts/$', viewWrapper(publishTexts)),


                       )

# patterns for blog
urlpatterns += patterns('',
                        (r'^home/$', viewWrapper(home)),
                        (r'^machine_learning/$', viewWrapper(machine_learning)),
                        (r'^twitter_visualization/$', viewWrapper(twitter_visualization)),
                        (r'^map_reduce/$', viewWrapper(map_reduce)),
                        )

# patterns for django_yaba
urlpatterns += patterns('',
                        url(r'^nocss/', include('django_yaba.urls')),
                        )


# patterns for admin
from django.contrib import admin

admin.autodiscover()

urlpatterns += patterns('',
                        (r'^admin/', include(admin.site.urls)),
                        )

urlpatterns += patterns('', (r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")) )

#
# # # redirect everything else
urlpatterns += patterns('',
                        (r'^/$',  redirect, {'page':"/~/"}),
                        (r'^$',  redirect, {'page':"/~/"}),
                        # (r'.*$',  redirect, {'page':"/home/"}),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


