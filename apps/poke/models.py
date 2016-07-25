from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


# Create your models here.

class UserManager(models.Manager):
	pass

class Pokemon(models.Model):
	name = models.CharField(max_length=250)
	hp = models.PositiveSmallIntegerField()
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
	userManager = UserManager()


class User(models.Model):
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	lvl = models.PositiveSmallIntegerField()
	p1 = models.ForeignKey(Pokemon)
	p2 = models.ForeignKey(Pokemon, related_name="Pokemon2")
	p3 = models.ForeignKey(Pokemon, related_name="Pokemon3")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userManager = UserManager()
	# objects = models.Manager()