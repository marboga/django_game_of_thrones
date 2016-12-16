from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from models import House
from ..regions.models import Region

def index(request):
	if request.method == 'POST':
		new_house = House.objects.create_house(request.POST)
		if new_house[0] == True: #this means we were successful
			print 'we rejoice!'
		else:
			context['errors'] = new_house[1]

	context = {
		'houses': House.objects.all(),
		'regions': Region.objects.all(),
	}
	return render(request, 'houses/index.html', context)

def delete(request, id):
	id = int(id)
	print House.objects.remove_house(id)
	return redirect('/')

def show(request, id):
	context = {
		'one_house': House.objects.get(id=id)
	}
	return render(request, 'houses/show.html', context)

def update(request, id):
	print request.method
	if request.method == 'POST':
		print request.POST
		house =  House.objects.update_house(request.POST)
		if not house[0]:
			messages.error(request, house[1])
	return redirect('houses:index')
