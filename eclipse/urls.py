
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views
from .import forms

urlpatterns = [
    
   path('', views.home, name = "home"), 
   path('learning/', views.learning, name = "learning"), 
   path('contact/',views.contact, name='contact'),
   path('single/', views.single, name = "single"), 
   path('blog/', views.blog, name = "blog"),
   path('articles/',views.articles, name ="articles"),
   path('projects/',views.projects, name ="projects"),
   path('photos/', views.photos, name = "photos"),
   path('morephotos/', views.morephotos, name = "morephotos"),
   path('services/', views.services, name = "services"),
   path('about/', views.about, name = "about"),
   path('portifolio/', views.portifolio, name = "portifolio"),
   path('email/',views.email, name ="email"),


   

]
