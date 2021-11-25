from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def new(request):
    form = CustomerForm()
    return render(request, "reserve/new.html",{"form":form})
