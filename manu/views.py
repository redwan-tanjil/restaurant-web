from django.shortcuts import render


def index(request):
    a='menu'
    return render(request,'menu.html',{'title':a})


def italian(request):
    a='italian food'
    return render(request,'italian.html',{"title":a})


def chinese(request):
    a='chinese food'
    return render(request,'italian.html',{"title":a})


def fast_food(request):
    a='ifast food'
    return render(request,'italian.html',{"title":a})