from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
	def validName(self, username):
		if len(username) < 2:
			return(False, "username")
		if len(User.objects.filter(username=username)) > 0:
			return(False, "usedname")
		return True
	def validEmail(self, email):
		if len(email) < 1:
			return(False, "email")
		elif not re.match(EMAIL_REGEX, email):
			return(False, "email")
		return True
	def validPass(self, pass1, pass2):
		if len(pass1) < 8:
			return(False, "pass1")
		if pass2 == pass1:
			return True
		else:
			return(False, "pass2")
	def validate(self, username, email, pass1, pass2):
		nameResults = User.userManager.validName(username)
		emailResults = User.userManager.validEmail(email)
		passResults = User.userManager.validPass(pass1, pass2)
		if nameResults==True:
			pass
		else:
			return nameResults
		if emailResults==True:
			pass
		else:
			return emailResults
		if passResults==True:
			pass
		else:
			return passResults
		pass1 = pass1.encode(encoding="utf-8", errors="strict")
		hashed = bcrypt.hashpw(pass1, bcrypt.gensalt())
		currentUser = User.objects.create(username=username, email=email, password=hashed)
		return(True, currentUser)
	def login(self, username, pass1):
		if len(User.objects.filter(username=username)) == 0:
			return (False, "username")
		else:
			userInfo = User.objects.filter(username=username)
		if bcrypt.hashpw(pass1.encode(encoding="utf-8", errors="strict"), userInfo[0].password.encode(encoding="utf-8", errors="strict")) == userInfo[0].password.encode(encoding="utf-8", errors="strict"):
			return True
		else:
			return (False, "pass")
	def imagegrab(self, id):
		for i in range(3):
			pass


# Create your models here.

class PokemonManager(models.Manager):
	def add(self, pokeid, name, hp, poketype, atk1power,atk2power,atk3power,atk4power,atk1name,atk2name,atk3name,atk4name,id):
		user= User.objects.get(id= id)
		print pokeid
		print atk3name
		print atk1power
		if user.p1 is None:
			pokemon1= Pokemon.objects.create(pokeid=pokeid,name=name, hp=hp, poketype=poketype,atk1power=atk1power, atk2power= atk2power, atk3power=atk3power,atk4power=atk4power,atk1name=atk1name, atk2name=atk2name, atk3name= atk3name, atk4name= atk4name)
			user.p1= pokemon1
			user.save()
			print user.p1.name
			print "user1"
		elif user.p2 is None:
			pokemon2= Pokemon.objects.create(pokeid=pokeid, name=name, hp=hp, poketype=poketype,atk1power=atk1power, atk2power= atk2power, atk3power=atk3power,atk4power=atk4power,atk1name=atk1name, atk2name=atk2name, atk3name= atk3name, atk4name= atk4name)
			user.p2= pokemon2
			print user.p2.name
			print "User2"
			user.save()
		elif user.p3 is None:
			pokemon3= Pokemon.objects.create(pokeid=pokeid, name=name, hp=hp, poketype=poketype,atk1power=atk1power, atk2power= atk2power, atk3power=atk3power,atk4power=atk4power,atk1name=atk1name, atk2name=atk2name, atk3name= atk3name, atk4name= atk4name)
			user.p3= pokemon3
			print user.p3.name
			print 'user3'
			user.save()
			return True
	def trade(self, user, userpoke, pokeid, name, hp, poketype, atk1power,atk2power,atk3power,atk4power,atk1name,atk2name,atk3name,atk4name):
		if 'p1' == 'p'+userpoke:
			user = User.objects.get(id=user)
			print '********', user.p1.name
			user.p1.name = name
			user.p1.pokeid = pokeid
			user.p1.hp = hp
			user.p1.poketype = poketype
			user.p1.atk1power = atk1power
			user.p1.atk2power = atk2power
			user.p1.atk3power = atk3power
			user.p1.atk4power = atk4power
			user.p1.atk1name = atk1name
			user.p1.atk2name = atk2name
			user.p1.atk3name = atk3name
			user.p1.atk4name = atk4name
			user.p1.save()
		elif 'p2' == 'p'+userpoke:
			user = User.objects.get(id=user)
			print '********', user.p2.name
			user.p2.name = name
			user.p2.pokeid = pokeid
			user.p2.hp = hp
			user.p2.poketype = poketype
			user.p2.atk1power = atk1power
			user.p2.atk2power = atk2power
			user.p2.atk3power = atk3power
			user.p2.atk4power = atk4power
			user.p2.atk1name = atk1name
			user.p2.atk2name = atk2name
			user.p2.atk3name = atk3name
			user.p2.atk4name = atk4name
			user.p2.save()
		elif 'p3' == 'p'+userpoke:
			user = User.objects.get(id=user)
			print '********', user.p3.name
			user.p3.name = name
			user.p3.pokeid = pokeid
			user.p3.hp = hp
			user.p3.poketype = poketype
			user.p3.atk1power = atk1power
			user.p3.atk2power = atk2power
			user.p3.atk3power = atk3power
			user.p3.atk4power = atk4power
			user.p3.atk1name = atk1name
			user.p3.atk2name = atk2name
			user.p3.atk3name = atk3name
			user.p3.atk4name = atk4name
			user.p3.save()

		return True

class Pokemon(models.Model):
	name = models.CharField(max_length=250)
	hp = models.PositiveSmallIntegerField()
	pokeid = models.PositiveSmallIntegerField(null=True)
	poketype = models.CharField(max_length=250)
	atk1name = models.CharField(max_length=250)
	atk1power = models.PositiveSmallIntegerField()
	atk2name = models.CharField(max_length=250, null=True)
	atk2power = models.PositiveSmallIntegerField(null=True)
	atk3name = models.CharField(max_length=250, null=True)
	atk3power = models.PositiveSmallIntegerField(null=True)
	atk4name = models.CharField(max_length=250, null=True)
	atk4power = models.PositiveSmallIntegerField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	pokemonManager = PokemonManager()
	objects = models.Manager()


class User(models.Model):
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	lvl = models.PositiveSmallIntegerField(default=1)
	p1 = models.ForeignKey(Pokemon, null=True)
	p2 = models.ForeignKey(Pokemon, related_name="Pokemon2", null=True)
	p3 = models.ForeignKey(Pokemon, related_name="Pokemon3", null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	objects = models.Manager()