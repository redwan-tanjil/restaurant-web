from django.shortcuts import render


def index(request):
    title='contact us'
    return render(request,'contact.html',{'title':title})