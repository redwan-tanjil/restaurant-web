from django.urls import path

from  . import views

urlpatterns=[
    path('',views.index),
    path('italian/',views.italian),
    path('chinese/',views.chinese),
    path('fastfood/',views.fast_food),
]