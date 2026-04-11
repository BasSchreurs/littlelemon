from django.shortcuts import render
from rest_framework import viewsets
from .models import Menu, MenuItem, Booking
from .serializers import MenuSerializer, MenuItemSerializer, BookingSerializer
from .forms import BookingForm

def index_view(request):
    return render(request, 'restaurant/index.html')

def menu_view(request):
    menus = Menu.objects.prefetch_related('items').all()
    return render(request, 'restaurant/menu.html', {'menus' : menus})

def about_view(request):
    return render(request, 'restaurant/about.html')

def book_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return render(request, 'restaurant/book.html', {
                'form': BookingForm(),
                'success': f"Thank you for booking at {booking.booking_date}!"
            })
    else:
        form = BookingForm()

    return render(request, 'restaurant/book.html', {'form': form})

class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

