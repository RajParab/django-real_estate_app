from django.shortcuts import render
from property.models import Property, Category
from clients.models import Client
from about.models import About
from django.db.models import Count
# Create your views here.

def homepage(request):
	template='home/home.html'
	clients=Client.objects.all()
	properties=Property.objects.all()
	categories=Category.objects.annotate(property_count=Count('property')).values('category_name','property_count','category_image')
	about_home=About.objects.all()[1]

	context={
				'clients_home':clients,
				'properties_home':properties,
				'categories_home':categories,
				'about_home':about_home,
	}

	return render(request, template,context)