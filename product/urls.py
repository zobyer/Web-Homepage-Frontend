from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='mobile'),
    path('log_in',views.log_in,name='log_in'),
    path('register',views.register,name='register')

]