from django.urls import path
from  . import views

urlpatterns = [path('create_booking/', views.create_booking),
               path('success/',views.booking_success,name='booking_success')

               ]