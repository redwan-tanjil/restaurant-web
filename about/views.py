from django.shortcuts import render


def index(request):
    title='about us'
    return render(request,'about.html',{'title':title})