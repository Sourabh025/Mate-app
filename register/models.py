from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
import datetime

class extrafields(models.Model):

	birthdate =  models.DateField(('DOB'))

	user=models.OneToOneField(User,related_name='extra',on_delete=models.CASCADE)
	# options=[('programming','Programming'),('maths','Maths'),('science','Science'),('medical','Medical')]
	interest=models.CharField(max_length=50)
	# option=[('amity,noida','Amity,Noida'),('dtu','DTU'),('iitd','IIT delhi')]
	campus=models.CharField(max_length=50)
	# optionloc=[('Noida','Noida'),('Delhi','Delhi'),('Mumbai','Mumbai')]
	location=models.CharField(max_length=50)
	
	def __str__(self):
		return '%s' % (self.user.username)	#this function returning name of user in profile model(on django profile option)
