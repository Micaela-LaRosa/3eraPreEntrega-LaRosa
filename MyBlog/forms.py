from django import forms
from django.utils import timezone

class UsersForm(forms.Form):
    name= forms.CharField(max_length=30)
    last_name= forms.CharField(max_length=30)
    email = forms.EmailField()

class PostsForm(forms.Form):
    title = forms.CharField(max_length=30)
    text = forms.CharField(max_length=200)
    publish_date = forms.DateTimeField(required=False, initial=timezone.now, widget=forms.DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}))
    modified_date = forms.DateTimeField(required=False, initial=timezone.now, widget=forms.DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}))

class CommentsForm(forms.Form):
    author = forms.CharField(max_length=50)
    text = forms.CharField(max_length=200)
    created_date = forms.DateTimeField(required=False, initial=timezone.now, widget=forms.DateTimeInput(format='%Y-%m-%d', attrs={'type': 'datetime-local'}))
    approved_comment = forms.BooleanField()

class CategoriesForm(forms.Form):
    name = forms.CharField(max_length=30)


    
