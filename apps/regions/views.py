from django.shortcuts import render, redirect



def index(request):
	print 'in another app!'
	return render(request, 'regions/index.html')

def create(request):
	print 'in create method'
	data = {
		'name': request.POST['name']
	}
	print Region.objects.create_region(request.POST)
	return redirect('houses:index')
