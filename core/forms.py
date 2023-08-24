from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True, max_length=200, label='', 
                           widget=forms.Textarea(
                               attrs={
                                   "placeholder": 'Enter your tweet here!',
                                   
                               }
                           ),
                           )
    
    class Meta:
        model = Tweet
        fields = ('body',)


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }

                                ))
    first_name = forms.CharField(min_length=1, max_length=15, widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }

                                ))
    last_name= forms.CharField(min_length=1, max_length=15, widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control'
                                }

                                ))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'