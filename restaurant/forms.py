from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking

class BookingForm(forms.ModelForm):
    booking_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']

    def clean_booking_date(self):
        date = self.cleaned_data['booking_date']

    def clean_booking_date(self):
        date = self.cleaned_data['booking_date']

        if date < timezone.now():
            raise ValidationError("Booking date cannot be in the past.")

        weekday = date.weekday()
        hour = date.hour

        if 0 <= weekday <= 4:
            if hour < 14 or hour >= 22:
                raise ValidationError("Bookings on Monday–Friday are allowed between 14:00 and 22:00.")
        elif weekday == 5:
            if hour < 14 or hour >= 23:
                raise ValidationError("Bookings on Saturday are allowed between 14:00 and 23:00.")
        else:
            if hour < 14 or hour >= 21:
                raise ValidationError("Bookings on Sunday are allowed between 14:00 and 21:00.")

        return date
