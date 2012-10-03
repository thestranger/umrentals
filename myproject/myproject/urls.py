from django.views.generic import list_detail
from listing.models import Listing
from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
listings_info = { 
    'queryset': Listing.objects.all()
    #'template_name' :
}

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myproject.views.home', name='home'),
    url(r'^listings/(?P<location>Commons|Courtyards|Varsity|View)/$', 'myproject.views.listing_by_building'),
    url(r'^listings/(?P<max_price>\d+)/$', 'myproject.views.listing_by_price'),
    url(r'^listings/$', list_detail.object_list,listings_info),
    url(r'^listing/(?P<listing_id>\d+)/$', 'myproject.views.listing'),
    url(r'^submit$', 'myproject.views.submitListing'),
    url(r'^about$', 'myproject.views.about'),
    url(r'^presentation$', 'myproject.views.presentation'),
    url(r'^contact/$', 'myproject.views.contact'),
    url(r'^commons=(?P<commons>(true|false))/courtyards=(?P<courtyards>(true|false))/varsity=(?P<varsity>(true|false))/view=(?P<view>(true|false))/(?P<startyear>(\d{4}|(any)))/(?P<startmonth>(\d{1,2}|(any)))/(?P<startday>(\d{1,2}|(any)))/(?P<endyear>(\d{4}|(any)))/(?P<endmonth>(\d{1,2}|(any)))/(?P<endday>(\d{1,2}|(any)))/(?P<pricerange>(all|less500|less1000|great1000))/(?P<numrooms>(1|2|3|4))/$', 'myproject.views.searchresults'),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')), #Don't add this line if you use django registration or userena for registration and auth.

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
