from django.contrib import admin
from django.urls import path
from bookings import views as booking_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', booking_views.home, name='home'),
    path('book/', booking_views.create_booking, name='create_booking'),
    path('success/', booking_views.booking_success, name='booking_success'),
    path('report/', booking_views.booking_report, name='booking_report'),
    path('analytics/', booking_views.booking_analytics, name='booking_analytics'),
    path('my-bookings/', booking_views.my_bookings, name='my_bookings'),
    path('table-analytics/', booking_views.table_analytics, name='table_analytics'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls')),
    path('users/', include('users.urls')),  # ✅ This is important
]
