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
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	fullname = forms.CharField(
		widget = forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder': 'Type your Fullname', 
			'id':'form_full_name',
			}
		)
	)
	email	 = forms.EmailField(
		widget = forms.EmailInput(
			attrs={
			'class':'form-control',
			'placeholder': 'Type your Email', 
			'id':'form_email',
			}
		)
	)
	content	 = forms.CharField(
		widget = forms.Textarea(
			attrs={
			'class':'form-control',
			'placeholder': 'Type your Content', 
			'id':'form_content',
			}
		)
	)

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if not "gmail.com" in email:
			raise forms.ValidationError('Email has to be gmail.com')

		return email

