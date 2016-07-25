from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

import re

# Create your views here.
def index(request):
	return render(request, 'poke/index.html')

def battle(request):

	
	user_id = request.session['id']

	context = {
		"user": User.userManager.all(id=user_id),
		"userPoke": User.userManager.filter(id=user_id),
		# "userPoke2": User.userManager.filter(id=user_id).p2,
		# "userPoke3": User.userManager.filter(id=user_id).p3,

		"opponent": User.userManager.all(id=id),
		"opponentPoke1": User.userManager.filter(id=id).p1,
		"opponentPoke2": User.userManager.filter(id=id).p2,
		"opponentPoke3": User.userManager.filter(id=id).p3,
	}

	return render(request, 'poke/battle.html', context)