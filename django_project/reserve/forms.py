from django import forms

from reserve.models import reserves

class CustomerForm(forms.ModelForm):
    class Meta:
        model = reserves
        fields = '__all__'