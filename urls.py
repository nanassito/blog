from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^view/(.+)$', 'blog.article.views.article_long_uri', name='longview'),
    url(r'^v/(\d+)$', 'blog.article.views.article_short_uri', name='shortview'),
    url(r'^$', 'blog.article.views.all_articles', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)
