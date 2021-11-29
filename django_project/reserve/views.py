from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import ReservationForm, SearchForm
from django.contrib import messages
from .models import Reservation
from table.models import Table
from django.urls import reverse
from urllib.parse import urlencode
from django.db.models import Q
from itertools import chain

from datetime import date, datetime, time, timedelta

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def search_table(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #form.save()
            #username = form.cleaned_data.get('username')
            #tableList = Table.objects.all()

            #tableList = list(tableList)
            #ocuppiedSet = Reservation.objects.values_list('table_id', flat=True) 
            #ocuppiedSet = Reservation.objects.values_list('table_id', flat=True)
            #ocuppiedList = list(ocuppiedSet)
            #ocuppiedList = list(chain(tableList,reservationList))
            #tables = Table.objects.exclude(tableId__in = list(Reservation.objects.values_list('table_id', flat=True)))
            custom_number = form.cleaned_data.get('custuomer_number')
            date = form.cleaned_data.get('date')
            arrive = form.cleaned_data.get('arrive')
            duration = form.cleaned_data.get('duration')

            print(custom_number)
            print(date)
            print(arrive)
            print(duration)
            dt = datetime.combine(date,arrive)
            print(dt)
            out = dt + timedelta(hours=int(duration))
            print(out)

            
            tables = Table.objects.exclude(pk__in = list(Reservation.objects.values_list('table_id', flat=True)))

            print(date)

            messages.success(request, f'You can select the tables below')
            
            return render(request, 'reserve/search_result.html', {'form': form, 'tables': tables})
            #return redirect('login')

            #base_url = reverse('reservation-create')
            #query_string =  urlencode({'first_name': 'Dong'})
            #url = '{}?{}'.format(base_url, query_string)

            # request.session["duration"] = form.cleaned_data.get('duration')
            # request.session["duration"] = form.cleaned_data.get('duration')
            # request.session["duration"] = form.cleaned_data.get('duration')
            # request.session["duration"] = form.cleaned_data.get('duration')
            # request.session["duration"] = form.cleaned_data.get('duration')
            # return redirect('reservation-create')
    else:
        form = SearchForm()
    return render(request, 'reserve/search.html', {'form': form})
    


class ReservationCreateView(CreateView):
    #fields = ['first_name', 'last_name', 'phone', 'date', 'arrive', 'duration']

    form_class = ReservationForm
    success_url = 'list'

    # def form_valid(self, form):
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('table_search')

    # #initial = {"first_name": request.}
    # def get_initial(self):
    #     return {
    #          'duration': self.request.session['duration']
    #     }

    #initial = {"first_name": request.}
    def get_initial(self):
        date = self.request.GET['date']
        arrive = self.request.GET['arrive']
    
        duration = self.request.GET['duration']
        dt = datetime.combine(datetime.strptime(date, '%Y-%m-%d').date(),datetime.strptime(arrive, '%H:%M').time())
        out = dt + timedelta(hours=int(duration))


        return {
             'duration': self.request.GET['duration'],
             'date': self.request.GET['date'],
             'arrive': self.request.GET['arrive'],
             'customer_number':self.request.GET['customer_number'],
             'table_id':self.request.GET['table_id'],
             'come':dt,
             'out':out
        }

class TableListView(ListView):
    model = Table
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reserve/reservation_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reservations'