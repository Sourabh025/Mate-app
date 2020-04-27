from django.shortcuts import render

from .models import Post


# Create your views here.

def home(request):
	
	context={

		'posts':Post.objects.all()
		#creating an object of a Post model 
	
	}

	return render(request,"homefeed.html",context)