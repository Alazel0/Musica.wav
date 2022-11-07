from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ComentForm
from .models import Comentarios

# Create your views here.

def Home(request):
	return render(request,'Home.html')

def Registrarse(request):

	if request.method == 'GET':
		return render(request,'Musica.html', {
			'form': UserCreationForm
		})

	else:
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(username=request.POST['username'], password= request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('Descargas')
			except IntegrityError:
				return render(request,'Musica.html', {
					'form': UserCreationForm,
					"error": 'Username already exists'
				})
		return render(request,'Musica.html', {
			'form': UserCreationForm,
			"error": 'Password do not match'
		})

def Descargas(request):
	comentarios = Comentarios.objects.all()

	return render(request, 'Descargas.html', {'comentarios': comentarios})

def comentarios(request):
	if request.method == 'GET':
		return render(request,'comentarios.html', {
				'form': ComentForm
			})
	else:
		try:
			form = ComentForm(request.POST)
			new_coment = form.save(commit=False)
			new_coment.user = request.user
			new_coment.save()
			return redirect('Home')
		except ValueError:
			return render(request,'comentarios.html', {
					'form': ComentForm,
					'error': 'Please provide valida data'
				})



def cerrar_sesion(request):
	logout(request)
	return redirect('Home')

def ingresar(request):
	if request.method == 'GET':
		return render(request, 'ingresar.html', {
				'form': AuthenticationForm
			})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

		if user is None:
			return render(request, 'ingresar.html', {
					'form': AuthenticationForm,
					'error': 'Username or password is incorrect'
				})

		else:
			login(request, user)
			return redirect('Home')