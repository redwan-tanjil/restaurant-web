from django.contrib import admin
from .models import Reservation


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'num' , 'date' , 'guest' , 'time')


admin.site.register(Reservation ,ReservationAdmin)