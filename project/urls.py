from django.conf.urls import *
from project.admin import blogging_admin
from libazpm.contrib.blogging.feeds import BlogFeed
from django.views.generic.base import RedirectView

feeds = {
    'rss': BlogFeed,
}

urlpatterns = patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(blogging_admin.urls)),
    (r'^f/(?P<blog>[\w-]+)/$', BlogFeed()),
    (r'^b/', include('libazpm.contrib.blogging.urls', namespace="blogging")),
    (r'^$', RedirectView.as_view(url="/b/"))
)
