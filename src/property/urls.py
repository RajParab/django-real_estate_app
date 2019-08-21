from django.urls import path
from . import views


app_name='property'

urlpatterns = [
				path('',views.propertyList, name='property_list'),
				path('<int:id>',views.propertyDetail, name='property_detail'),
			]