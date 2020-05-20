#forms.py are used to create forms using existing fields of db tables

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from userprofile.models import profile  # import profile model from userprofile
from .models import extrafields
#extending UserCreationForm  


options=[('programming','Programming'),('maths','Maths'),('science','Science'),('medical','Medical')]

option=[('amity,noida','Amity,Noida'),('dtu','DTU'),('iitd','IIT delhi')]

optionloc=[('Noida','Noida'),('Delhi','Delhi'),('Mumbai','Mumbai')]

class reg(UserCreationForm):
    # options=[('programming','Programming'),('maths','Maths'),('science','Science'),('medical','Medical')]
    # interest=forms.CharField(required=True,widget=forms.Select(choices=options))
    # last_name=forms.CharField()

    email=forms.EmailField()
    # adding extra fields to the UserCreationForm 

    #constructor used to remove help text from the signup page
    # def __init__(self, *args, **kwargs):

    #     super(UserCreationForm, self).__init__(*args, **kwargs)

    #     # setting helptext to None
    #     for fieldname in ['username', 'password1', 'password2']:
    #         self.fields[fieldname].help_text = None

    class Meta:
        
        model=User
        fields=["username","email","password1","password2"]
    
# here UserForm and ProfileForm are just forms not tables in database
# but all these fields inside these forms are related to tables  

class UserForm(forms.ModelForm):
    class Meta:
        
        #this form using User table from our DB
        
        model=User


        #specifying fields of our form
        fields=[

            'username',
            'email',    
            
      
        ]
      
        # specify help text we need for 
        help_texts={

            'username' : "enter name",
            'email':"enter your email",
            
        }

#extending profile model
#creating a form for the profile edit 

class ProfileForm(forms.ModelForm):
    
    class Meta:

        # note here model name is profile that we had defined in our userprofile app
        # insimple words profile is a table inside our database

        model=profile

        #fields take list of fields that we need in our form 

        fields=[

            'bio',
            'profile_image',
        
        ]

        help_texts={

            'bio' : "Update your bio",
            
        }

        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }



# Meta gives us fields that Already existed in our model or table


class signfields(forms.ModelForm):
    birthdate=forms.DateField(required=True,widget = forms.SelectDateWidget(years=range(1990, 2010)))
    interest=forms.CharField(required=True,widget=forms.Select(choices=options))
    location=forms.CharField(required=True,widget=forms.Select(choices=optionloc))
    campus=forms.CharField(required=True,widget=forms.Select(choices=option))

    class Meta:
        model=extrafields

        fields=['birthdate','interest','campus','location']


