from django import forms
from stackoverflowapp.models import MyUser
from django.contrib.auth.forms import UserCreationForm
from stackoverflowapp.models import Question
from tkinter import Widget

class RegistrationForm(UserCreationForm):
    widgets={    
        "password1":forms.TextInput(attrs={"class":"form-control"}),
        "password2":forms.TextInput(attrs={"class":"form-control"})
        }
    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","email","phone","profile_pic","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "profile_pic":forms.FileInput(attrs={"class":"form-control"}),
        }
        
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=[
            "description",
            "image",
        ] 
        
        widgets={
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }
        
class AnswerForm(forms.Form):
    answer=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))