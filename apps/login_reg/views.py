from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	users = User.objects.all()
	context = {
		'users': users
	}
	return render(request, 'login_reg/index.html', context)

def register(request):
	if request.method == 'POST':
		response = User.objects.validate_registration(request.POST)
		if response[0] == True:
			print response[1]
			print response[1].first_name
			request.session['first_name'] = response[1].first_name
			return redirect('login_reg:success')
		else:
			for err in response[1]:
				messages.error(request, err)
	return redirect('login_reg:index')

def success(request):
	return redirect('houses:index')

def login(request):
	if request.method == "GET":
		messages.warning(request, 'error')
		return redirect('login_reg:index')
	else:
		(valid, data) = User.objects.validate_login(request.POST)
		if valid:
			return redirect('login_reg:success')
		else:
			for error in data:
				messages.warning(request, error)
		return redirect('login_reg:index')
