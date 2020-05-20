from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, ListView
from register.forms import ProfileForm,UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required #decorator
from django.views import generic
from userprofile.models import profile
from django.contrib import messages
from django.http import HttpResponseRedirect
from post.models import Post

# Create your views here.


@login_required
def search(request):
	if request.method=="POST":
		srch=request.POST['srh'] #fetching srh variable input from placeholder html file
		print("inside search")
		if srch:
			match=User.objects.filter(Q(username__icontains=srch))
			match1=Post.objects.filter(Q(title__icontains=srch))
			#match contains all the data of searched user ie it is an object
			#select * from User where username =srch
			print(match)

			print(match1)
			return render(request,'search.html',{'sr':match,'sr1':match1})
			
			match="Nothing Found"
			messages.error(request,'no result found')
		else:
			#if srch is None
			return HttpResponseRedirect("/search/")
	return render(request,'search.html')
	#return render first before function executes

def ProfileView(request,pk):
	# pk is passed through a template dynamic url hence we need to add to aurguments 
	# path('profile/<str:pk>/',s.Profilesearch,name='profileview')
	# href="{% url 'profileview' profile.id %}" inside search template
	
	user=User.objects.get(pk=pk)
	arg={'user':user}
	return render(request,'profileSearch.html/',arg)