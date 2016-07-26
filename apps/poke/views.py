from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse

import re

# Create your views here.
def index(request):
	return render(request, 'poke/index.html')

def register(request):
	valid = User.userManager.validate(request.POST['username'], request.POST['email'], request.POST['pass1'], request.POST['pass2'])
	if valid[0]==True:
		request.session['username'] = valid[1].username
		request.session['id'] = valid[1].id
		return redirect(reverse('poke_papi'))
	else:
		if valid[1] == "name":
			messages.info(request, "Name must be at least 3 characters")
		elif valid[1] == "username":
			messages.info(request, "Username must be at least 3 character")
		elif valid[1] == "usedname":
			messages.info(request, "Sorry, that Username has already been taken")
		elif valid[1] == "email":
			messages.info(request, "Please enter a valid email")
		elif valid[1] == "pass1":
			messages.info(request, "Password must be at least 8 characters")
		elif valid[1] == "pass2":
			messages.info(request, "Passwords do not match")
		return redirect('/')

def login(request):
	if User.userManager.login(request.POST['username'], request.POST['pass1']) == True:
		user = User.objects.filter(username=request.POST['username'])
		request.session['username'] = user[0].username
		request.session['id'] = user[0].id
		return redirect(reverse('poke_dashboard'))
	else:
		messages.warning(request, 'Username and Password do not match')
		return redirect(reverse('poke_index'))

def papi(request):
	
	return render(request, 'poke/papi.html')

def pokedex(request):
	if request.method=="POST":
		id= request.session['id']
		name= request.POST['name']
		hp= request.POST['hp']
		poketype= request.POST['poketype']
		atk1name= request.POST['atk1name']
		atk1power= request.POST['atk1power']
		full=Pokemon.pokemonManager.add(name,hp,poketype,atk1name,atk1power,id)
		if full:
			return redirect(reverse('poke_dashboard'))
		messages.info(request, 'You added '+ name)
	return redirect(reverse ('poke_papi'))	

def dashboard(request):
	
	return render(request, 'poke/dashboard.html')


