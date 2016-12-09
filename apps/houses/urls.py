from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^house/(?P<house>\w+)$', views.show),
	url(r'^update/(?P<id>\d+)$', views.update),
	url(r'^house/(?P<id>\d+)/delete$', views.delete),

]
