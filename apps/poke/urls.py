from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'poke_index'),
	url(r'^battle$', views.battle),
]