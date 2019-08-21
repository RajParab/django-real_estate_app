from django.shortcuts import render
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q

# Create your views here.
def propertyList(request):
	properties=Property.objects.all()
	categories=Category.objects.all()

	templates='property/list.html'

	search_query=request.GET.get('q')
	property_type_query=request.GET.getlist('category', None)

	if search_query or property_type_query:
		properties=properties.filter(
			Q(name__icontains = search_query) |
			Q(location__icontains = search_query) &
			Q(types__icontains = property_type_query)

			)

	context={
				'properties':properties,
				'categories':categories,
	}

	return render(request, templates, context)

def propertyDetail(request, id):
	property_details=Property.objects.get(id=id)

	if request.method=='POST':
		form= ReserveForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form= ReserveForm()

	
	templates='property/detail.html'

	context={
				'property_details':property_details,
				'form':form,
	}

	return render(request, templates, context)

