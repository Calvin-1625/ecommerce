"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

def home_page(request):
	# print(request.session.get('first_name', 'Unknown'))
	context = {
		"title":"Hello World",
		"content":"Welcome to the home page",
	}
	if request.user.is_authenticated:
		context["premium_content"] = "Yeaahhh"
	return render(request, "home_page.html", context)

def about(request):
	context = {
		"title":"About Page",
		"content":"Welcome to the about page"
	}
	return render(request, "home_page.html", context)

def contact(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title":"Contact",
		"content":"Welcome to the contact page",
		"form": contact_form,
		# "brand": "New Brand Name",
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)


	# if request.method == "POST":
	# 	#print(request.POST)
	# 	print(request.POST.get('Fullname'))
	# 	print(request.POST.get('Email'))
	# 	print(request.POST.get('Content'))

	return render(request, "contact/view.html", context)

