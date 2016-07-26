from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'poke_index'),
	url(r'^register$', views.register, name = 'poke_register'),
	url(r'^login$', views.login, name = 'poke_login'),
	url(r'^papi$', views.papi, name = 'poke_papi'),
	url(r'^dashboard$', views.dashboard, name = 'poke_dashboard'),
	url(r'^battle$', views.battle, name = 'poke_battle'),
	url(r'^(?P<userpokeid>\d+)/atk$', views.userATK, name = 'poke_atk')
]