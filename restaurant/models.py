from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,related_name='items')
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - ${self.price}"

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.no_of_guests} - {self.booking_date}"