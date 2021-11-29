from django import forms

from .models import reserves

class CustomerForm(forms.ModelForm):
    class Meta:
        model = reserves
        fields = ['Reservee_Last_name', 'Reservee_First_name', 'table_id', 'Tele_Num', 'Reservation_ID']
