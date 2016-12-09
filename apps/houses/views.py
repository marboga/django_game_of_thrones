from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.

houses = [
	{
		'name': 'Baratheon',
		'sigil': 'Stag',
		'colors': ['green', 'gold'],
		'motto': 'Ours is the Fury'
	},
	{
		'name': 'Lannister',
		'sigil': 'Lion',
		'colors': ['gold', 'crimson'],
		'motto': 'Hear Me Roar'
	},
]

try:
	delete_db = default_storage.delete('./database.py')
except:
	pass
save_db = default_storage.save('./database.py', ContentFile(houses))

def index(request):

	if request.method == 'POST':
		print request, "\n","*"*50,"\n" , request.POST
		new_house = {}
		new_house['name'] = request.POST['name']
		new_house['sigil'] = request.POST['sigil']
		new_house['motto'] = request.POST['motto']
		new_house['colors'] = []
		new_house['colors'].append(request.POST['color1'])
		new_house['colors'].append(request.POST['color2'])
		print new_house, "h*50"*50
		houses.append(new_house)
		delete_db
		save_db


	context = {
		'houses': houses,
	}
	return render(request, 'houses/index.html', context)

def show(request, house):
	house = int(house)
	print house
	if house > len(houses):
		messages.warning(request, 'House not found in the database')
		return redirect('/')

	houses[house]['id'] = house

	context = {
		'one_house': houses[house]
	}
	return render(request, 'houses/index.html', context)

def update(request, id):
	id = int(id)
	if request.method == "POST":
		curr_house = houses[id]
		print curr_house

		curr_house['name'] = request.POST['name']
		curr_house['sigil'] = request.POST['sigil']
		curr_house['motto'] = request.POST['motto']
		curr_house['colors'] = []
		curr_house['colors'].append(request.POST['color1'])
		curr_house['colors'].append(request.POST['color2'])
		curr_house['id'] = id

		houses[id] = curr_house

	return redirect('/')

def delete(request, id):
	id = int(id)
	houses.pop(id)
	print houses
	return redirect('/')
