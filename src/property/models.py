from django.db import models

# Create your models here.

class Property(models.Model):

	TYPES=[
			('Rent','Rent'),
			('Sale', 'Sale'),

	]


	name=models.CharField(max_length=50)
	category=models.ForeignKey('Category', on_delete=models.SET)
	price=models.DecimalField(max_digits=10, decimal_places=2)
	area=models.DecimalField(max_digits=10, decimal_places=2)
	types=models.CharField(max_length=10, choices=TYPES)
	bath=models.IntegerField()
	bed=models.IntegerField()
	garage=models.IntegerField()
	image=models.ImageField(upload_to='property/', null=True)
	created_on=models.TimeField(auto_now=True)
	updated_on=models.TimeField(auto_now_add=True)
	location=models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name='Property'
		verbose_name_plural='Properties'


class Category(models.Model):
	category_name=models.CharField(max_length=10)
	category_image=models.ImageField(upload_to='category/')

	def __str__(self):
		return self.category_name


	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'


class Reserve(models.Model):
	name=models.CharField(max_length=30)
	start_date=models.DateField(null=True)
	end_date=models.DateField(null=True)
	message=models.TextField(null=True)

	def __str__(self):
		return self.name

