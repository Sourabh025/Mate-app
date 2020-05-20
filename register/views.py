from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate

from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin   #--- this mixins required to check if user is logged in or not---

from django.contrib import messages

from .forms import ProfileForm,UserForm  #--- import feilds from forms.py to used in templates forms---

from django.contrib.auth.models import  User

from post.models import Post

from .forms import reg,signfields

from .models import extrafields

from userprofile.models import profile  #--- importing from userprofile app model to here---

from django.views.generic import TemplateView, CreateView

# Create your views here.

def registration(request):
    print("check1")
    form=reg() # user creation form should be intialised empty in the begining otherwise signup will not work
    sign=signfields()
    if request.method=="POST":
        form=reg(request.POST)
        sign=signfields(request.POST)
        print("inside request")
        if form.is_valid() and sign.is_valid():
            print("getting form")
            form.save()
            # best way to solve user_id can't be null (foreign key (child model))
            new_user = form.save()
            f = sign.save(commit=False) #commit false returns object before saving to the db
            if f.user_id is None:
                f.user_id = new_user.id #user_id is by default coloumn name.
            f.save()
            #saving foreign key correctly according to current user

            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            email=form.cleaned_data.get('email')
            user=authenticate(username=username,password=raw_password)
            print("Signup successfull")
            return redirect('login')
    else:
        print("Form not saved")
        form=reg()
        sign=signfields()
        print(User.objects.all())  #printing all the users from auth table 
        print(User.objects.filter(username="user"))
        x=User.objects.first()
        print(x.id)
    return render(request,"register.html",{"form": form,"sign":sign})


#profile functionality starts from here
# we can also use function for below class with @Login_required decorator instead of LoginRequiredMixin
class ProfileView(LoginRequiredMixin, TemplateView):  #this will render profile of user onlyif user is loggedin 
    template_name='profile.html'

#if user is logged in then this class render profile_update form if he wants to edit his/her profile 
class ProfileUpdateView(LoginRequiredMixin,TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'profile_update.html'  # this will open template if user logged in 

    #this post method will work if user enter submit button with some data in profile_update template form and save and authenticate data
    def post(self, request):

        post_data = request.POST or None #storing post request  data that is entered by a user
        file_data= request.FILES  or None # storing file in this case file is image
        user_form = UserForm(post_data, instance=request.user)  #storing userform data which is entered by user for user model 
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)  #loading profile_form with all data to profile model

        #UserForm and ProfileForm are two different froms defined in forms.py
        print("Next check for validation")
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()  #save user_form
            profile_form.save() #save profileform
            print("form saved")
            messages.success(request, 'Your profile successfully updated!')
            return render(request,'profile.html')#after submit button user will be redirected to his newly updated profile
        
        else:
            messages.error(request,'sorry some error occured')
        #context return dictonary of forms to the template profile_update    
        context = self.get_context_data(
                                        user_form=user_form,           #context will be used when we use variable in html file {form.as_p}
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)


    #get method will run post method without validation of user data
    def get(self, request, *args, **kwargs):        #get method will run when user request is get 
        return self.post(request, *args, **kwargs)

    #both get and post methods will run only if user is logged in