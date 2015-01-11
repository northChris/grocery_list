from django.conf.urls import patterns, url
urlpatterns = patterns(
    'items.views',
    url(r'^$', 'home_page'),
)
