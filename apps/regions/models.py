from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RegionManager(models.Manager):
	def create_region(self, data):
		print 'in create_region method'
		errors = []
		if not data['name']:
			errors.append('name field is empty')
			return (False, errors)
		print data
		print self.create(name=data['name'])


class Region(models.Model):
	name = models.CharField(max_length=200)
	trade_goods = models.CharField(max_length=200)

	objects = RegionManager()
