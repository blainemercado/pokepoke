from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'poke_index'),
	url(r'^register$', views.register, name = 'poke_register'),
	url(r'^login$', views.login, name = 'poke_login'),
	url(r'^papi$', views.papi, name = 'poke_papi'),
	url(r'^dashboard$', views.dashboard, name = 'poke_dashboard'),
	url(r'^prebattle$', views.prebattle, name = 'poke_lineup'),
	url(r'^prebattlepick$', views.prebattlepick, name = 'poke_battlepick'),
	url(r'^battle$', views.battle, name = 'poke_battle'),
	url(r'^atk$', views.userATK, name = 'poke_atk'),
	url(r'^OppATK$', views.OppATK, name = 'poke_def'),
	url(r'^papi/pokedex$', views.pokedex, name = 'poke_pokedex'),
	url(r'^youwon$', views.youwon, name = "poke_won"),
	url(r'^youlose$', views.youlose, name = "poke_lose"),
	url(r'^dashboard/(?P<id>\d+)$', views.dashboard, name = 'poke_dashboard'),
	url(r'^rivals$', views.rivals, name = 'poke_rivals'),
	url(r'^logout$', views.logout, name = 'poke_logout')
]