from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, ListView
from register.forms import ProfileForm,UserForm
from django.contrib.auth.mixins import LoginRequiredMixin 
# Create your views here.
	
class search(CreateView):
    model = User
    template_name = 'search.html'
    fields="__all__" #include all fields
    def get_queryset(self):
        query = self.request.GET.get('q')
        print("inside")
        object_list = User.objects.filter(
            Q(username__icontains=query)
        )
        print(object_list)
        return object_list

def search(request):
	if request.method=="POST":
		srch=request.POST['srh'] #fetching srh variable input from placeholder html file
		print("inside search")
		if srch:
			match=User.objects.filter(Q(username__icontains=srch))
			print(match)

			if match:
				return render(request,'search.html',{'sr':match})
			else:
				message.error(request,'no result found')
		else:
			#if srch not null
			return HttpResponseRedirect("/search/")

	return render(request,'search.html') 