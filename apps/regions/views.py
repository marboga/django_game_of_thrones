from django.shortcuts import render, redirect
from models import Region
from ..houses.models import House
# Create your views here.

def index(request):
	print 'in regions:index'
	print request
	regions = Region.objects.all()
	houses = House.objects.all()
	context = {
		'regions': regions,
		'houses': houses,
	}
	return render(request, 'regions/index.html', context)

def create(request):
	print 'in regions:create method'
	if request.method == 'POST':
		print 'calling create method'
		Region.objects.create_region(request.POST)

	return redirect('regions:index')

def connect(request):
	if request.method == 'POST':
		print 'in connection method', request.POST

		House.objects.bridge_connections(request.POST)


	return redirect('regions:index')
