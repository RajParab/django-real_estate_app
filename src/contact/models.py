from django.db import models

# Create your models here.
class Contact(models.Model):
	address=models.CharField(max_length=100)
	email=models.EmailField()
	contact_no=models.CharField(max_length=15)

	