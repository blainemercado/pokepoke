from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from random import randint

import re

def index(request):
	return render(request, 'poke/index.html')

def preprebattle(request, id):
	request.session['opponent_id'] = id

	return redirect('/prebattle')

def prebattle(request):

	request.session['oppATKchoice'] = "TAUNT"

	request.session['count'] = 1
	request.session['OpCount'] = 1
	print request.session['opponent_id']
	opponent = User.userManager.get(id=request.session['opponent_id'])

	request.session['oppPoke1'] = opponent.p1
	request.session['oppPoke2'] = opponent.p2
	request.session['oppPoke3'] = opponent.p3

	user_id = request.session['id']
	user= User.objects.filter(id=user_id)
	context = {
		"user": User.userManager.get(id=user_id),
		"userPoke1": User.userManager.get(id=user_id).p1,
		"userPoke2": User.userManager.get(id=user_id).p2,
		"userPoke3": User.userManager.get(id=user_id).p3,
		"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
		"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
		"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",
	}

	return render(request, "poke/prebattle.html", context)

def prebattlepick(request):
	user_id = request.session['id']
	if request.method == "POST":
		if 'poke1' in request.POST:
			pick = User.userManager.get(id=user_id).p1
			request.session['currentHP'] = request.session['oppPoke1'].hp
			print "POKEMON 1"
			user= User.objects.filter(id=user_id)
			context = {
				"firstpick": pick,
				"user": User.userManager.get(id=user_id),
				"userPoke1": User.userManager.get(id=user_id).p1,
				"userPoke2": User.userManager.get(id=user_id).p2,
				"userPoke3": User.userManager.get(id=user_id).p3,
				"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
				"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
				"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",
			}
			request.session['initPokemon'] = pick
			request.session['MyHP'] = request.session['initPokemon'].hp
			request.session['secondPokemon'] = User.userManager.get(id=user_id).p2
			request.session['thirdPokemon'] = User.userManager.get(id=user_id).p3
			print request.session['initPokemon'].name
			print "***************"
			print pick.name
			return render(request, "poke/prebattle.html", context)
		elif 'poke2' in request.POST:
			pick = User.userManager.get(id=user_id).p2
			request.session['currentHP'] = request.session['oppPoke1'].hp
			print "POKEMON 2"
			user= User.objects.filter(id=user_id)
			context = {
				"firstpick": pick,
				"user": User.userManager.get(id=user_id),
				"userPoke1": User.userManager.get(id=user_id).p1,
				"userPoke2": User.userManager.get(id=user_id).p2,
				"userPoke3": User.userManager.get(id=user_id).p3,
				"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
				"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
				"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",
			}
			request.session['initPokemon'] = pick
			request.session['MyHP'] = request.session['initPokemon'].hp
			request.session['secondPokemon'] = User.userManager.get(id=user_id).p1
			request.session['thirdPokemon'] = User.userManager.get(id=user_id).p3
			print pick.name
			return render(request, "poke/prebattle.html", context)
		elif 'poke3' in request.POST:
			pick = User.userManager.get(id=user_id).p3
			request.session['currentHP'] = request.session['oppPoke1'].hp
			print "POKEMON 3"
			user= User.objects.filter(id=user_id)
			context = {
				"firstpick": pick,
				"user": User.userManager.get(id=user_id),
				"userPoke1": User.userManager.get(id=user_id).p1,
				"userPoke2": User.userManager.get(id=user_id).p2,
				"userPoke3": User.userManager.get(id=user_id).p3,
				"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
				"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
				"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",
			}
			request.session['initPokemon'] = pick
			request.session['MyHP'] = request.session['initPokemon'].hp
			request.session['secondPokemon'] = User.userManager.get(id=user_id).p1
			request.session['thirdPokemon'] = User.userManager.get(id=user_id).p2
			print pick.name
			return render(request, "poke/prebattle.html", context)

	return render(request, "poke/prebattle.html")

def battle(request):
	user_id = request.session['id']
	user = User.objects.filter(id=user_id)
	Opp_id = request.session['opponent_id']
	opponent = User.objects.filter(id=Opp_id)

	context = {
		"user": User.userManager.get(id=user_id),
		"userPoke1": User.userManager.get(id=user_id).p1,
		"userPoke2": User.userManager.get(id=user_id).p2,
		"userPoke3": User.userManager.get(id=user_id).p3,
		"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
		"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
		"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",

		"opponent": User.userManager.get(id=request.session['opponent_id']),
		"opponentPoke1": User.userManager.get(id=request.session['opponent_id']).p1,
		"opponentPoke2": User.userManager.get(id=request.session['opponent_id']).p2,
		"opponentPoke3": User.userManager.get(id=request.session['opponent_id']).p3,
		"opp1": "poke/images/" + str(opponent[0].p1.pokeid) + ".png",
		"opp2": "poke/images/" + str(opponent[0].p2.pokeid) + ".png",
		"opp3": "poke/images/" + str(opponent[0].p3.pokeid) + ".png",	
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
		return redirect('/gainlevel')

def OppATK(request):

	user_id = request.session['id']
	randomNum = randint(0,100)
	print ("randomNum:", randomNum)
	print "******************"
	print ("opponent atk choice 1:", request.session['oppPoke1'].atk1name)
	print ("opponent atk choice 2:", request.session['oppPoke1'].atk2name)
	print ("opponent atk choice 3:", request.session['oppPoke1'].atk3name)
	print ("opponent atk choice 4:", request.session['oppPoke1'].atk4name)
	if randomNum < 25:
		theirAttack = User.userManager.get(id=request.session['opponent_id']).p1.atk1power
		print ("theirAttack 1:", theirAttack)
		request.session['oppATKchoice'] = request.session['oppPoke1'].atk1name
	elif randomNum >24 and randomNum<51:
		theirAttack = User.userManager.get(id=request.session['opponent_id']).p1.atk2power
		print ("theirAttack 2:", theirAttack)
		request.session['oppATKchoice'] = request.session['oppPoke1'].atk2name
	elif randomNum >50 and randomNum<76:
		theirAttack = User.userManager.get(id=request.session['opponent_id']).p1.atk3power
		print ("theirAttack 3:", theirAttack)
		request.session['oppATKchoice'] = request.session['oppPoke1'].atk3name
	elif randomNum >75:
		theirAttack = User.userManager.get(id=request.session['opponent_id']).p1.atk4power
		print ("theirAttack 4:", theirAttack)
		request.session['oppATKchoice'] = request.session['oppPoke1'].atk4name

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
		return redirect('/youlose')

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
	user= User.objects.get(id= request.session['id'])
	print user.lvl
	context={
	"users": User.objects.get(id=request.session['id']).lvl
	}
	return render(request, 'poke/papi.html', context)

def pokedex(request):
	if request.method=="POST":
		id= request.session['id']
		pokeid=request.POST['pokeid']
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

def otherdashboard(request,id):
	user= User.objects.filter(id=id)
	request.session['opponent_id']= id
	print request.session['opponent_id']
	context = {
 		"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
 		"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
 		"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",
 		"user": User.objects.filter(id=id)
  	}
	return render(request, 'poke/otherdashboard.html', context)

def dashboard(request):
	user= User.objects.filter(id=request.session['id'])
	context = {
 		"p1": "poke/images/" + str(user[0].p1.pokeid) + ".png",
 		"p2": "poke/images/" + str(user[0].p2.pokeid) + ".png",
 		"p3": "poke/images/" + str(user[0].p3.pokeid) + ".png",
 		"user": User.objects.filter(id=request.session['id'])
  	}
	return render(request, 'poke/dashboard.html', context)	

def gainlevel(request):
	user=User.objects.get(id=request.session['id'])
	print user.lvl
	user.lvl= user.lvl+1
	print user.lvl
	user.save()
	return redirect('/youwon')
def youwon(request):
	
	context={
	"users": User.objects.get(id=request.session['id'])
	}
	return render(request, 'poke/youwon.html',context)

def youlose(request):
	context={
	"users": User.objects.filter(id=request.session['id'])
	}
	return render(request, 'poke/youlose.html',context)

def rivals(request):
	context={
 	"users": User.objects.exclude(id=request.session['id'])#, "pokemon": 'test'
 	}
 	return render(request, 'poke/rivals.html', context)

def logout(request):

	for key in request.session.keys():
		del request.session[key]

	return redirect('/')