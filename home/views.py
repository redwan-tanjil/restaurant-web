from django.shortcuts import render
from .models import Subscriber
from .models import Massage

import smtplib


def home(request):

    if request.method == 'POST' :
        a = request.POST['email']
        b = Subscriber.objects.create(email=a)
        b.save()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('redwan.tanjil@gmail.com' , '02 03 2002')
        subject = 'subscribe'
        body = 'thanks for subscribe \n from tanjil'
        msg = f'subject:{subject}\n\n{body}'
        server.sendmail(
            'redwan.tanjil@gmail.com' ,
            a,
            msg
        )

    if Massage.objects.filter(num=1).exists():

        for person in Subscriber.objects.all():
            text = Massage.objects.get(num=1).text
            sub = Massage.objects.get(num=1).sub
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('redwan.tanjil@gmail.com', '02 03 2002')
            subject = sub
            body = text
            msg = f'subject:{subject}\n\n{body}'
            server.sendmail(
                'redwan.tanjil@gmail.com',
                person.email,
                msg
            )
        Massage.objects.filter(num=1).delete()

    title = "welcome to our site"
    return render(request , 'home.html' , {'title':title})
