from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
	first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'First Name', 'autocomplete':'off', 'autofocus':'on'}))
	last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Last Name', 'autocomplete':'off'}))
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Username', 'autocomplete':'off'}))
	email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email', 'autocomplete':'off'}))
	password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))



class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    password = None




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','gender']

    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'col-5'}))
    gender = forms.ChoiceField(required=False, choices=[('female', 'Female'), ('male', 'Male')], widget=forms.RadioSelect())



