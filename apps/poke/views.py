from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from random import randint

import re

# Create your views here.
def index(request):
	return render(request, 'poke/index.html')

def prebattle(request):
	request.session['count'] = 1
	request.session['OpCount'] = 1
	opponent_id = 3 #CHANGE THIS TO OPPONENT ID
	opponent = User.userManager.get(id=opponent_id)

	request.session['oppPoke1'] = opponent.p1
	request.session['oppPoke2'] = opponent.p2
	request.session['oppPoke3'] = opponent.p3

	user_id = request.session['id']
	
	context = {
		"user": User.userManager.get(id=user_id),
		"userPoke1": User.userManager.get(id=user_id).p1,
		"userPoke2": User.userManager.get(id=user_id).p2,
		"userPoke3": User.userManager.get(id=user_id).p3,
	}

	return render(request, "poke/prebattle.html", context)

def prebattlepick(request):
	user_id = request.session['id']
	if request.method == "POST":
		if 'poke1' in request.POST:
			pick = User.userManager.get(id=user_id).p1
			request.session['currentHP'] = request.session['oppPoke1'].hp
			request.session['MyHP'] = request.session['initPokemon'].hp
			print "POKEMON 1"
			context = {
				"firstpick": pick,
				"user": User.userManager.get(id=user_id),
				"userPoke1": User.userManager.get(id=user_id).p1,
				"userPoke2": User.userManager.get(id=user_id).p2,
				"userPoke3": User.userManager.get(id=user_id).p3,
			}
			request.session['initPokemon'] = pick
			request.session['secondPokemon'] = User.userManager.get(id=user_id).p2
			request.session['thirdPokemon'] = User.userManager.get(id=user_id).p3
			print request.session['initPokemon'].name
			print "***************"
			print pick.name
			return render(request, "poke/prebattle.html", context)
		elif 'poke2' in request.POST:
			pick = User.userManager.get(id=user_id).p2
			request.session['currentHP'] = request.session['oppPoke1'].hp
			request.session['MyHP'] = request.session['initPokemon'].hp
			print "POKEMON 2"
			context = {
				"firstpick": pick,
				"user": User.userManager.get(id=user_id),
				"userPoke1": User.userManager.get(id=user_id).p1,
				"userPoke2": User.userManager.get(id=user_id).p2,
				"userPoke3": User.userManager.get(id=user_id).p3,
			}
			request.session['initPokemon'] = pick
			request.session['secondPokemon'] = User.userManager.get(id=user_id).p1
			request.session['thirdPokemon'] = User.userManager.get(id=user_id).p3
			print pick.name
			return render(request, "poke/prebattle.html", context)
		elif 'poke3' in request.POST:
			pick = User.userManager.get(id=user_id).p3
			request.session['currentHP'] = request.session['oppPoke1'].hp
			request.session['MyHP'] = request.session['initPokemon'].hp
			print "POKEMON 3"
			context = {
				"firstpick": pick,
				"user": User.userManager.get(id=user_id),
				"userPoke1": User.userManager.get(id=user_id).p1,
				"userPoke2": User.userManager.get(id=user_id).p2,
				"userPoke3": User.userManager.get(id=user_id).p3,
			}
			request.session['initPokemon'] = pick
			request.session['secondPokemon'] = User.userManager.get(id=user_id).p1
			request.session['thirdPokemon'] = User.userManager.get(id=user_id).p2
			print pick.name
			return render(request, "poke/prebattle.html", context)

	return render(request, "poke/prebattle.html")

def battle(request):
	opponent_id = 3 #CHANGE THIS TO OPPONENT ID
	user_id = request.session['id']

	context = {
		"user": User.userManager.get(id=user_id),
		"userPoke1": User.userManager.get(id=user_id).p1,
		"userPoke2": User.userManager.get(id=user_id).p2,
		"userPoke3": User.userManager.get(id=user_id).p3,

		"opponent": User.userManager.get(id=opponent_id),
		"opponentPoke1": User.userManager.get(id=opponent_id).p1,
		"opponentPoke2": User.userManager.get(id=opponent_id).p2,
		"opponentPoke3": User.userManager.get(id=opponent_id).p3,	
	}

	return render(request, 'poke/battle.html', context)

def userATK(request):

	user_id = request.session['id']

	print request.session['oppPoke1'].name
	attack = User.userManager.get(id=request.session['id']).p1.atk1power
	print ("Attack power is:", attack)


	print request.session['count']
	if request.session['currentHP'] > 0:
		request.session['currentHP'] -= (randint(0, attack/2))
		return redirect('/OppATK')

	elif request.session['currentHP'] <= 0 and request.session['count'] == 1:
		request.session['currentHP'] = request.session['oppPoke2'].hp
		request.session['count'] = 2
		request.session['oppPoke1'] = request.session['oppPoke2']
		print ("opponent HP:", request.session['currentHP'], request.session['oppPoke1'].name)
		return redirect('/OppATK')

	elif request.session['currentHP'] <= 0 and request.session['count'] == 2:
		request.session['currentHP'] = request.session['oppPoke3'].hp
		request.session['count'] = 3
		request.session['oppPoke1'] = request.session['oppPoke3']
		print ("opponent HP:", request.session['currentHP'], request.session['oppPoke1'].name)
		return redirect('/OppATK')

	elif request.session['currentHP'] <= 0 and request.session['count'] == 3:
		return redirect('/youwon')

def OppATK(request):
	opponent_id = 3

	user_id = request.session['id']

	theirAttack = User.userManager.get(id=opponent_id).p1.atk1power

	if request.session['MyHP'] > 0:
		request.session['MyHP'] -= (randint(0, theirAttack/2))

	elif request.session['MyHP'] <= 0 and request.session['OpCount'] == 1:
		request.session['MyHP'] = request.session['secondPokemon'].hp
		request.session['OpCount'] = 2
		request.session['initPokemon'] = request.session['secondPokemon']
		print ("my HP:", request.session['MyHP'], request.session['initPokemon'].name)
		return redirect('/battle')

	elif request.session['MyHP'] <= 0 and request.session['OpCount'] == 2:
		request.session['MyHP'] = request.session['thirdPokemon'].hp
		request.session['OpCount'] = 3
		request.session['initPokemon'] = request.session['thirdPokemon']
		print ("my HP:", request.session['MyHP'], request.session['initPokemon'].name)
		return redirect('/battle')

	elif request.session['MyHP'] <= 0 and request.session['OpCount'] == 3:
		return redirect('/youlost')

	print ("my HP", request.session['MyHP'])

	return redirect('/battle')

def register(request):
	print "pre check"
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
			return redirect(reverse('poke_dashboard'))
		messages.info(request, 'You added '+ name)
	return redirect(reverse ('poke_papi'))	

def dashboard(request):
	context = {
		"user": User.objects.filter(id=request.session['id'])
	}
	return render(request, 'poke/dashboard.html', context)

def youwon(request):
	return redirect('/dashboard')

def youlose(request):
	return redirect('/dashboard')

def rivals(request):
	context = {
		"users": User.objects.all()
	}
	return render(request, "poke/rivals.html", context)

def logout(request):
	del request.session['id']
	del request.session['username']

	return redirect('/index')