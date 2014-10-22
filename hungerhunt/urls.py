from django.conf.urls import patterns, include, url
from django.contrib import admin
from hunger import views as hungerViews
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hungerhunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^home/', hungerViews.hunger, name='home'),
	url(r'^register/', hungerViews.register, name='register'),
	url(r'^delete/', hungerViews.delete, name='delete'),
	url(r'^vote/', hungerViews.vote, name='vote'),
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
	#url(r'^addfood/', hungerViews.createFood, name='addFood'),
)
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
