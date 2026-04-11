from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet
from . import views

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', views.index_view, name='index'),
    path('menu/', views.menu_view, name='menu'),
    path('about/', views.about_view, name='about'),
    path('book/', views.book_view, name='book'),
] + router.urls  # append API routes
