from django.shortcuts import render
from django.http import HttpResponse, Http404 

def home(request):
	return render(request, 'headerbody/pagecontent/home.html')

def about(request):
	return render(request, 'headerbody/pagecontent/about.html')

def contact(request):
	return render(request, 'headerbody/pagecontent/contact.html')
