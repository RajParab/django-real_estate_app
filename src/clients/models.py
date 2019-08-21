from django.db import models

# Create your models here.
class Client(models.Model):
	name=models.CharField(max_length=30)
	image=models.ImageField(upload_to='clients/',null=True)
	title=models.CharField(max_length=70)
	insta_handle=models.URLField(max_length=70)

	def __str__(self):
		return self.name

