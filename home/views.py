from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post
# Create your views here.





def home(request):
	# passing dictionary
	context={

		'posts':Post.objects.all()

		#creating an object of a Post model 

	}

	return render(request,"homefeed.html",context)


# def home(request):
   
#         return render(request,"new.html")
