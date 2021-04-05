from courses.models import Java
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from eclipse.forms import ContactForm, JavaForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.views.generic import ListView, TemplateView


# Create your views here.
def learning(request):
     return render(request, 'eclipse/index.html')

def home(request):
    return render(request, 'eclipse/home.html')

def single(request):
    return render(request, 'eclipse/single.html')

def singleblog(request):
    return render(request, 'eclipse/single-blog.html')

def portifolio(request):
    return render(request, 'eclipse/portifolio.html')


def photos(request):
    return render(request, 'eclipse/photos/photos.html')

def morephotos(request):
    return render(request, 'eclipse/photos/single.html')

def services(request):
    return render(request, 'eclipse/photos/services.html')

def about(request):
    return render(request, 'eclipse/photos/about.html')

def email(request):
    res = send_mail("contacting me","hello, I would like to join your group", "eliudmaina064@gmail.com", ['mainachiurieliud@gmail.com'], fail_silently=False)
    
    return render(request, 'eclipse/contact.html')


def contact(request):
    submitted = False
    if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():
             cd = form.cleaned_data
             con = get_connection('django.core.mail.backends.console.EmailBackend')
             res = send_mail("contacting me","hello, I would like to join your group", "eliudmaina064@gmail.com", ['mainachiurieliud@gmail.com'],fail_silently=False)
             return HttpResponseRedirect('/contact?submitted=True')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
             submitted = True
 
    return render(request, 
                'eclipse/form.html', 
                {'form': form, 'submitted': submitted})


def projects(request):
    return render(request, 'eclipse/blog/blogpost.html')

def articles(request):
    return render(request, 'eclipse/blog/blogslist.html')
                  


def blog(request):
    return render(request, 'eclipse/blog/index.html')


