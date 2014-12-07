from django.conf.urls import patterns, include, url
from django.contrib import admin
from hunger import views as hungerViews
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout_then_login


urlpatterns = patterns('',
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', hungerViews.hunger, name='home'),
    url(r'^register/', hungerViews.register, name='register'),
    url(r'^recommend/', hungerViews.recommend, name='recommend'),
    url(r'^friend/', hungerViews.friendRecommend, name='friend_recommend'),
    url(r'^delete/', hungerViews.delete, name='delete'),
    url(r'^vote/', hungerViews.vote, name='vote'),
    url(r'^trends/', hungerViews.trends, name='trends'),
    url(r'^socialNetworkingUpdate/', hungerViews.socialNetworkingUpdate, name='socialNetworkingUpdate'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^addfood/', hungerViews.foodNutrition, name='createfood'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
)
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))