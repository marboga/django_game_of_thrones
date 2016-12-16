from __future__ import unicode_literals

from django.db import models
from ..regions.models import Region


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

	def bridge_connections(self, data):
		errors = []
		# try:
		house = int(data['house'])
		region = int(data['region'])
		# except:
			# errors.append('this is impossible!')
		this_house = House.objects.get(id=house)
		this_region = Region.objects.get(id=region)
		print this_house.name, this_region.name
		this_house.region.add(this_region)
		this_house.save()


class House(models.Model):
	name = models.CharField(max_length=200)
	sigil = models.CharField(max_length=200)
	color1 = models.CharField(max_length=200)
	color2 = models.CharField(max_length=200)
	motto = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	region = models.ManyToManyField(Region, related_name="house_region")
	objects = HouseManager()
