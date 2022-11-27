from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

from account.forms import AccountAuthenticationForm, RegistrationForm
from account.models import Customer
from personal.views import get_redirect_if_exists

def logout_view(request):
	logout(request)
	return redirect("home")

def login_check(request):
	context = {}
	form = AccountAuthenticationForm(request.POST)

	destination = get_redirect_if_exists(request)
	if form.is_valid():
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(email=email, password=password)

		if user:
			login(request, user)
			context["success_message"] = "Login Valid"
			# if destination:
			# 	return redirect(destination)
			# return redirect("home")
	
	context['login_form'] = form
	return render(request, 'account/partial_login_form_error.html', context)

def register_check(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))
	form = RegistrationForm(request.POST)

	destination = get_redirect_if_exists(request)
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')

			account = authenticate(email=email, password=raw_password)
			login(request, account)
			customer = Customer(account=account)
			customer.save()

			context["success_message"] = "Register Valid"

			# destination = kwargs.get("next")
			# if destination:
			# 	return redirect(destination)
			# return redirect('home')
		else:
			context['login_form'] = form

	else:
		form = RegistrationForm()
		context['login_form'] = form
	return render(request, 'account/partial_login_form_error.html', context)



