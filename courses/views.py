from courses.forms import courseForm
from django.shortcuts import render, redirect
from .models import Java


def courses(request):
    return render(request, 'courses/courses.html')

def java(request):
    return render(request, 'courses/java.html')
    
def web(request):
    return render(request, 'courses/web.html')

def python(request):
    return render(request, 'courses/python.html')

def javascript(request):
    return render(request, 'courses/javascript.html')

def django(request):
    return render(request, 'courses/django.html')

def courseform(request):
    form = courseForm()

    todo_list = Java.objects.filter(title ='Arrays in java')[:5]
    
    

    context = { 'todo_list': todo_list , 'form': form}
    
 
    if request.method == 'POST':
        form = courseForm(request.POST)

        if form.is_valid():

            form = form.save()

            return redirect('/contact/')

        else:
            print(form.errors)

    return render(request, 'courses/add_category.html', context)
   
