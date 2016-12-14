from __future__ import unicode_literals
from django.db import models


class RegionManager(models.Manager):
	def create_region(self, data):
		errors = []
		print data
		if not data['name']:
			errors.append('Name must exist')

		if not errors:
			# try:
			region = self.create(name=data['name'])
			print region
			return (True, region)
			# except:
			# 	print 'error'
			# 	return (False, ['unknown db error'])
		else:
			return (False, errors)

class Region(models.Model):
	name = models.CharField(max_length=200)
	trade_goods = models.CharField(max_length=200)
	objects = RegionManager()

class HouseManager(models.Manager):
	def create_house(self, data):
		print data
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

	def remove_house(self, id):
		errors = []
		try:
			print 'deleting maybe'
			deleted = self.get(id=id).delete()
		except:
			deleted = ["This is no good"]
			print "whoooo nelly bad deleteds"
		return (True, deleted)

	def update_house(self, data):
		try:
			house = self.get(id=data['id'])
			print 'house', house
			house.name = data['name']
			house.sigil = data['sigil']
			house.color1 = data['color1']
			house.color2 = data['color2']
			house.motto = data['motto']
			house.save()
			return (True, house)
		except House.DoesNotExist:
			print 'doesnt exist'
		return (False, "it doesn't exist")

class House(models.Model):
	name = models.CharField(max_length=200)
	sigil = models.CharField(max_length=200)
	color1 = models.CharField(max_length=200)
	color2 = models.CharField(max_length=200)
	motto = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = HouseManager()
