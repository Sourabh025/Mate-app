
#forms.py are used to create forms using existing fields of db tables

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from userprofile.models import profile  # import profile model from userprofile

#extending UserCreationForm  

class reg(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    # adding extra fields to the UserCreationForm 

    #constructor used to remove help text from the signup page
    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)

        # setting helptext to None
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
        

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
            'location',
            'birth_date',
            'profile_image',
        
        ]

# Meta gives us fields that Already existed in our model or table