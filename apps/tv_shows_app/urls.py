from django.conf.urls import url
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new_show),
    url(r'^(?P<id>\d+)$', views.show_show),
    url(r'^(?P<id>\d+)/edit$', views.edit_show),
    url(r'^(?P<id>\d+)/update$', views.edit_show),
    url(r'^(?P<id>\d+)/delete$', views.delete_show)
    # url(r'^$', views.index)
]