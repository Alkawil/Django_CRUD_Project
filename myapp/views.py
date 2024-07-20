from django.shortcuts import render,get_object_or_404,redirect
from .forms import BookingForm
from .models import Booking, Category

# Create your views here.
from django.http import HttpResponse


def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    context = {"form" : form}
    return render(request, 'create_booking.html', context)

def booking_success(request):
    return HttpResponse("Booking created successfully!")