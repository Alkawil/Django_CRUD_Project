from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields ='__all__'
        widgets = {
            'reservation_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # HTML5 datetime picker
        }
    