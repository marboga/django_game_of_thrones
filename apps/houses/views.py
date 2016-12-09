from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from models import House

# Create your views here.




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







def show(request, house):
	house = int(house)
	print house
	if house > len(houses):
		messages.warning(request, 'House not found in the database')
		return redirect('/')



	context = {
		'one_house': "sdga"
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
