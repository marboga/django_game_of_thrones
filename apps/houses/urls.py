from django.conf.urls import url

from .views import index, show, update, delete

app_name = 'houses'
urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^house/(?P<id>\w+)$', show, name='show'),
	url(r'^update/(?P<id>\d+)$', update, name='update'),
	url(r'^house/(?P<id>\d+)/delete$', delete, name='delete'),
]
