from django.shortcuts import render
from myapp.forms import BookingForm

# Create your views here.
from django.http import HttpResponse

def drinks(request,drink_name):
    drink = {'mocha': 'type of coffee','tea' :'type of beverage','lemonade':'type of refreshment'}
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2>" +f"<p style=color:cyan;>{choice_of_drink}</p>")


def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)