from django.urls import path
from  . import views

urlpatterns = [path('', views.create_booking),
               path('success/<int:pk>/',views.booking_success,name='booking_success'),
               path('list/',views.booking_list,name='booking_list'),
               path('details/<int:pk>/',views.booking_details,name='booking_details'),
               path('details/<int:pk>/edit',views.booking_update,name='booking_update'),


               ]