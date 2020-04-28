from django.shortcuts import render

from .models import Post

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

def home(request):
	
	context={

		'posts':Post.objects.all()

		#creating an object of a Post model 
	
	}
	return render(request,"homefeed.html",context)


#alternative way to function home 
class PostView(generic.ListView):
	model=Post
	template_name="homefeed.html"
	context_object_name='posts'
	ordering=["-dateposted"]


	#note model,template_name,context_object_name,ordering are pre-defined
	#use of space and tab together illegal in python acc to PEP8


#in every class model is the most important part because it automate things for us 

class PostDetailView(generic.DetailView):
	model=Post
	template_name="postdetail.html"


#create new post 
class PostCreateView(LoginRequiredMixin,generic.CreateView):
	model=Post
	fields=['title','content','image','tag']
	template_name="post_form.html"
	context_object_name='post'

	#checking for user wheather user is valid or not 
	#form valid is a function inside a class of LoginRequiredMixin

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)


#updateview will be same as a  createview it automatically put things for us 
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
	model=Post
	fields=['title','content','image','tag']
	template_name="post_form.html"
	context_object_name='post'

	#checking for user wheather user is valid or not to update post
	#form_valid is function provided by LoginRequiredMixin 
	#form is a data inside the form submitted by a user 
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)  #super refering to parent class ie LoginRequiredMixin's some class that has form_valid function

	# test_func is a function provided by UserPassesTestMixin API 
	def test_func(self):

		post=self.get_object() #object of UserPassesTestMixin 
		
		#post variable contains the data(post model) of user who posted any post post
		#self is a instance of a request that is associated with the UserPassesTextMixin

		if self.request.user==post.author:
			return True
		else:
			return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
	model=Post
	fields=['title','content','image','tag']
	template_name="post_confirm_delete.html"
	context_object_name='post'
	success_url="/home"

	def test_func(self):

		post=self.get_object() #object of UserPassesTestMixin 
		#post variable contains the data(post model) of user who posted any post post
		#self is a instance of a request that is associated with the UserPassesTextMixin
		if self.request.user==post.author:
			return True
		else:
			return False
