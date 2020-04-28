from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

from django.urls import reverse
# Create your models here.

class Post(models.Model):
	title= models.CharField(max_length=100)
	tag=models.CharField(max_length=100)
	content=models.TextField()
	interest=models.CharField(max_length=100,default="")
	dateposted=models.DateTimeField(default=timezone.now)  #note now is afunction but we dont need to execute so dont use ()
	author=models.ForeignKey(User,on_delete=models.CASCADE) #creating one to many relation with the User
	image=models.ImageField(default=None,upload_to="Books")  #no default image required

	#__str__ returns the object string representation 
	
	def __str__(self):  
		return self.title

	#get absolute reverse the link to the newly created post
	#we just reversing url to thatnewly created post 
	def get_absolute_url(self):

		return reverse('post-detail',kwargs={'pk':self.pk})