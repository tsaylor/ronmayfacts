from django.conf.urls.defaults import *

urlpatterns = patterns('facts.views',
    # Example:
    # (r'^ronmayfacts/', include('ronmayfacts.foo.urls')),
    (r'^$', 'main'),
    (r'^r.$', 'autoreload'),
    (r'^facts/(?P<fact_id>\d+)/$', 'detail'),   # fact permalinks
    (r'^facts/submit/$', 'submit'),	# fact submission form
)
