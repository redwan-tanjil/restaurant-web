from django.shortcuts import render
from .models import Reservation


def index(request):

    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['num']
        d = request.POST['guest']
        e = request.POST['date']
        f = request.POST['time']
        bb=Reservation.objects.create(name=a,email=b,num=c,guest=d,date=e,time=f)
        bb.save()
    aq='make your reservation here'
    return render(request,'reservation.html',{'title':aq})

