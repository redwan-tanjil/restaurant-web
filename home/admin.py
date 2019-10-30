from django.contrib import admin
from .models import Subscriber
from .models import Massage

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email' ,)


class MassageAdmin(admin.ModelAdmin):
    list_display = ('text' ,'sub')


admin.site.register(Subscriber,SubscriberAdmin)

admin.site.register(Massage,MassageAdmin)