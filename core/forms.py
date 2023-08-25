from typing import Any, Optional
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

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


class UpdateUserForm(UserChangeForm):
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
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'form-control'
                                        }
                                    ))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'form-control'
                                        }
                                    ))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'form-control'
                                        }
                                    ))
    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']
    
    def __init__(self, user: AbstractBaseUser | None, *args: Any, **kwargs: Any) -> None:
        super().__init__(user, *args, **kwargs)
    