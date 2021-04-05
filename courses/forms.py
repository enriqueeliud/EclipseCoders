
from django import forms
from courses.models import Java

class courseForm(forms.Form):
    created = forms.DateField()
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Java
        fields = ['title']
