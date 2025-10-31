from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.create_booking, name='create_booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('report/', views.booking_report, name='booking_report'),
    path('analytics/', views.booking_analytics, name='booking_analytics'),
    path('table-analytics/', views.table_analytics, name='table_analytics'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
