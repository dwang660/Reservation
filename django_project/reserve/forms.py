from django import forms
from django.contrib.auth.models import User
#from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Reservation

DURATION_CHOICES = [(1, '1 hour'), (2, '2 hour'), (3, '3 hour'), (4, '4 hour'), (5, '5 hour'), (6, '6 hour')]

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class DateInput(forms.DateInput):
    input_type = "date"
    
class TimeInput(forms.TimeInput):
    input_type = "time"

class SearchForm(forms.Form):
    duration = forms.ChoiceField(required=False, widget=forms.Select, choices=DURATION_CHOICES)
    # name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)

    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    # favorite_colors = forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.Select,
    #     choices=FAVORITE_COLORS_CHOICES,
    # )

    date = forms.DateField(widget=DateInput)
    arrive = forms.TimeField()
    customer_number = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["arrive"].widget = TimeInput()
        # self.fields["end"].widget = DateInput()
        # self.fields["opening"].widget = TimeInput()
        # self.fields["closing"].widget = TimeInput()
        # self.fields["vernissage"].widget = DateTimeInput()
        # self.fields["vernissage"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        # self.fields["finissage"].widget = DateTimeInput()
        # self.fields["finissage"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['first_name', 'last_name', 'phone', 'date', 'arrive', 'duration', 'customer_number', 'table_id', 'table2nd_id', 'come', 'out' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["arrive"].widget = TimeInput()
        self.fields["date"].widget = DateInput()
        self.fields['table2nd_id'].required = False
        # self.fields["opening"].widget = TimeInput()
        # self.fields["closing"].widget = TimeInput()
        # self.fields["vernissage"].widget = DateTimeInput()
        # self.fields["vernissage"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        # self.fields["finissage"].widget = DateTimeInput()
        # self.fields["finissage"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
