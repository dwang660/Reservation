from django.contrib import admin

# Register your models here.
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'table_id', 'table2nd_id', 'customer_number')
admin.site.register(Reservation, ReservationAdmin)