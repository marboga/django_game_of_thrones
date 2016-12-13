from __future__ import unicode_literals

from django.db import models



# Create your models here.

class HouseManager(models.Manager):
	def create_house(self, data):
		errors = []
		if not data['name']:
			errors.append('name must not be empty')
		if not data['sigil']:
			errors.append('sigil must not be empty')
		if not data['color1']:
			errors.append('color1 must not be empty')
		if not data['color2']:
			errors.append('color2 must not be empty')
		if not data['motto']:
			errors.append('motto must not be empty')

		if not errors:
			print "no errors yet", data
			new_house = self.create(
				name=data['name'],
				sigil=data['sigil'],
				color1=data['color1'],
				color2=data['color2'],
				motto=data['motto']
			)
			return (True, new_house)
		else:
			return (False, errors)

class House(models.Model):
	name = models.CharField(max_length=200)
	sigil = models.CharField(max_length=200)
	color1 = models.CharField(max_length=200)
	color2 = models.CharField(max_length=200)
	motto = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	objects = HouseManager()

class Region(models.Model):
	name = models.CharField(max_length=200)
	trade_goods = models.CharField(max_length=200)
