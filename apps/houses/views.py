from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from models import House

def index(request):
	if request.method == 'POST':
		new_house = House.objects.create_house(request.POST)
		if new_house[0] == True: #this means we were successful
			print 'we rejoice!'
		else:
			context['errors'] = new_house[1]

	context = {
		'houses': House.objects.all(),
	}
	return render(request, 'houses/index.html', context)
