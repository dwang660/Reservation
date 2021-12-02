from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


FAVORITE_PAYMENT_CHOICES = [
    ('Cash', 'Cash'),
    ('Credit Card', 'Credit Card'),
    ('check', 'Check'),
]

class ProfileUpdateForm(forms.ModelForm):
    prefer_payment = forms.ChoiceField(required=False, widget=forms.Select, choices=FAVORITE_PAYMENT_CHOICES)
    
    The_same_as_mailing_address = forms.BooleanField(required=False)

    The_same_as_mailing_address = forms.DateField(required=False, widget=forms.CheckboxInput(attrs={'onClick': 'myFunction();'}))


    class Meta:
        model = Profile
        fields = ['phone', 'mailing_addresss', 'The_same_as_mailing_address', 'billing_addresss', 'prefer_payment']