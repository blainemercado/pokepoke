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


# Create your models here.
class PokemonManager(models.Manager):
	def add(self, name, hp, poketype,atk1name,atk1power,id):
		user= User.objects.get(id= id)
		#print user.p1.name
		if user.p1 is None:
			pokemon1= Pokemon.objects.create(name=name, hp=hp, poketype=poketype,atk1name=atk1name, atk1power= atk1power)
			user.p1= pokemon1
			user.save()
			print user.p1.name
			print "user1"
		elif user.p2 is None:
			pokemon2= Pokemon.objects.create(name=name, hp=hp, poketype=poketype,atk1name=atk1name, atk1power= atk1power)
			user.p2= pokemon2
			print user.p2.name
			print "User2"
			user.save()
		elif user.p3 is None:
			pokemon3= Pokemon.objects.create(name=name, hp=hp, poketype=poketype,atk1name=atk1name, atk1power= atk1power)
			user.p3= pokemon3
			print user.p3.name
			print 'user3'
			user.save()
			return True
		return False		
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