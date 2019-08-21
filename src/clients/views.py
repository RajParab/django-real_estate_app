from django.shortcuts import render

# Create your views here.
from .models import Client

def client_list(request):
	clients=Client.objects.all()

	template='clients/list.html'

	context={
				'clients':clients
	}

	return render(request, template, context)