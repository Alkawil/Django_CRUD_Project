from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'guest_count', 'reservation_time', 'comments', 'category']
        widgets = {
            'reservation_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


    