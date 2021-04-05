from django import forms
from courses.models import Java

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your Email Address')
    subject = forms.CharField(max_length=100)    
    message = forms.CharField(widget=forms.Textarea)
    
class JavaForm(forms.Form):
    created = forms.DateField()
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Java
        fields = ['title']
