from django.urls import path
from . import views


app_name='clients'
urlpatterns=[
			path('', views.client_list, name='client_list'),

]