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
		return redirect('dashboard/'+str(request.session['id']))
	else:
		messages.warning(request, 'Username and Password do not match')
		return redirect(reverse('poke_index'))

def papi(request):
	
	return render(request, 'poke/papi.html')

def pokedex(request):
	if request.method=="POST":
		pokeid= request.POST['pokeid']
		print request.POST['pokeid']
		id= request.session['id']
		name= request.POST['name']
		hp= request.POST['hp']
		poketype= request.POST['poketype']
		atk1power= request.POST['atk1power']
		atk2power= request.POST['atk2power']
		atk3power= request.POST['atk3power']
		atk4power= request.POST['atk3power']
		atk1name= request.POST['atk1name']
		atk2name= request.POST['atk2name']
		atk3name= request.POST['atk3name']
		atk4name= request.POST['atk4name']

		full=Pokemon.pokemonManager.add(pokeid,name,hp,poketype,atk1power,atk2power,atk3power,atk4power,atk1name,atk2name,atk3name,atk4name,id)
		if full:
			return redirect('/dashboard/'+str(request.session['id']))
		# else:
			# messages.info(request, "your roster is already full")
			# return redirect('/dashboard/'+str(request.session['id']))
		messages.info(request, 'You added '+ name)
	return redirect(reverse ('poke_papi'))	


def dashboard(request, id):
	user = User.objects.filter(id=id)
	context = {
		"user": User.objects.filter(id=id),
		"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
		"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
		"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png"
	}
	return render(request, 'poke/dashboard.html', context)

def rivals(request):
	# User.objects.filter(id='')
	
	context={
	"users": User.objects.exclude(id=request.session['id'])#, "pokemon": 'test'
	}
	return render(request, 'poke/rivals.html', context)

def logout(request):
	del request.session['id']
	del request.session['username']
	return redirect('/')



