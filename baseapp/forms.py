from .models import Note
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm



class CreateNoteForm(ModelForm):

    title = forms.CharField(max_length=15,required=True, widget=forms.TextInput(attrs={'class': 'form-control','id':'titletext'}))
    body = forms.CharField(max_length=80, required=True, help_text='Option',widget=forms.TextInput(attrs={'class': 'form-control','id':'bodytext'}))
    
    class Meta:
        model = Note
        fields = ['title', 'body', 'publish_as']



