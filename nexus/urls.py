"""
nexus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin

from django.urls import path,include

from register import views as v

from home import views as h

from userprofile import views as p

from register import views as pr

from post.views import PostView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

from post import views as post

from search import views as s

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',v.registration,name ='register'),
    #path('',v.registration,name='register1'),
    # path('home/',post.home,name='home'),
    path('home/',PostView.as_view(),name='post-create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/new/',PostCreateView.as_view(),name="post-form"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    #path('profile/',pr.ProfileUpdateView,name='profile'),  # wrong way to import class this will genrate an error because we are importing class as a function
    path('',include("django.contrib.auth.urls")),
    path('profile_update/', pr.ProfileUpdateView.as_view(), name='phome'), #always import class based view as it. other wise it will give error that one extra argument given
    path('profile/', pr.ProfileView.as_view(), name='prhome'),
    path('homefeed/',post.home,name='post'),  
    # path('search/',s.search.as_view(),name='search'),
    path('search/',s.search,name='search'),


]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

