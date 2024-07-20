from django.shortcuts import render,get_object_or_404,redirect
from .forms import BookingForm
from .models import Booking

# Create your views here.
from django.http import HttpResponse

# create

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_success',pk=booking.pk)
    else:
        form = BookingForm()

    return render(request, 'create_booking.html',{'form':form})

def booking_success(request,pk):
    booking = get_object_or_404(Booking,pk=pk)
    return render(request,'booking_success.html',{'booking':booking})

#Read
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request,'booking_list.html',{'bookings': bookings})

def booking_details(request,pk):
    booking = get_object_or_404(Booking,pk=pk)
    return render(request,'booking_details.html',{'booking':booking})

#update
def booking_update(request,pk):
    booking =get_object_or_404(Booking,pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST,instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_details',pk=pk)

    else:
        form = BookingForm(instance=booking)
    return render(request,'booking_update.html',{'form':form})