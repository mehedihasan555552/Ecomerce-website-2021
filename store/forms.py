from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class': 'input'}),
            'first_name':forms.TextInput(attrs={'class': 'input'}),
            'last_name':forms.TextInput(attrs={'class': 'input'}),
            'email':forms.EmailInput(attrs={'class': 'input'}),
            'password1':forms.PasswordInput(attrs={'class': 'input'}),
            'password2':forms.PasswordInput(attrs={'class': 'input'}),
        }



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','phone','address_line_1','address_line_2','state','city','country','order_note']
        


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review','rating']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        widgets = {
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class UserProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False, error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = UserProfile
        fields = ['address_line_1','address_line_2','city','state','phone','country','profile_pic']
        widgets = {
            'address_line_1':forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_2':forms.TextInput(attrs={'class': 'form-control'}),
            'state':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'country':forms.TextInput(attrs={'class': 'form-control'}),
            'city':forms.TextInput(attrs={'class': 'form-control'}),
            
           
            
        }