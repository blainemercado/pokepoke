from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'poke_index'),
	url(r'^register$', views.register, name = 'poke_register'),
	url(r'^login$', views.login, name = 'poke_login'),
	url(r'^papi$', views.papi, name = 'poke_papi'),
	url(r'^dashboard/(?P<id>\d+)$', views.dashboard, name = 'poke_dashboard'),
	url(r'^papi/pokedex$', views.pokedex, name = 'poke_pokedex'),
	url(r'^rivals$', views.rivals, name = 'poke_rivals'),
	url(r'^logout$', views.logout, name = 'poke_logout')
]