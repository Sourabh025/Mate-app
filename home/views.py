from django.shortcuts import render
from django.contrib.auth.models import User
from post.models import Post
# Create your views here.





def home(request):
	# passing dictionary
	print("Path of window is ",request.path)
	context={

		'posts':Post.objects.all()

		#creating an object of a Post model named posts

	}

	return render(request,"homefeed.html",context)


# def home(request):

#         return render(request,"new.html")
