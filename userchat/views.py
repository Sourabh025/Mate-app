from django.shortcuts import render

# Create your views here.



def share(request):
	return render(request,"room.html")