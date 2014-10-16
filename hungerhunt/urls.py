from django.conf.urls import patterns, include, url
from django.contrib import admin
from hunger import views as hungerViews

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hungerhunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', hungerViews.hunger),
	url(r'^restaurant/(?P<name>.+)/', hungerViews.restaurant),
)
