
from django.urls import path
from django.conf.urls import url

from courses import views

urlpatterns = [
   path('', views.courses, name = "courses"), 
   path('java/', views.java, name = "java"), 
   path('java/arrays/', views.courseform, name= "courseform"),
   path('web/', views.web, name = "web"), 
   path('python/', views.python, name = "python"), 
   path('javascript/', views.javascript, name = "javascript"), 
   path('django/', views.django, name = "django"), 


]
