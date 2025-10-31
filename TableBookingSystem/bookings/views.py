from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.db.models import Count
from .forms import BookingForm
from .models import Booking


def home(request):
    return render(request, 'bookings/home.html')


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            booking_time = form.cleaned_data['booking_time']

            # Check for existing booking
            if Booking.objects.filter(table=table, booking_time=booking_time).exists():
                messages.error(request, "Table already booked at this time.")
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.save()

                # Send email confirmation
                send_mail(
                    'Table Booking Confirmation',
                    f'Hi {request.user.username}, your booking for Table {table.number} at {booking_time} is confirmed!',
                    'your_gmail@gmail.com',
                    [request.user.email],
                    fail_silently=False,
                )
                return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


def booking_success(request):
    return render(request, 'bookings/success.html')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('my_bookings')


@staff_member_required
def booking_report(request):
    bookings = Booking.objects.select_related('user', 'table').order_by('-booking_time')
    return render(request, 'bookings/booking_report.html', {'bookings': bookings})


@staff_member_required
def booking_analytics(request):
    table_data = Booking.objects.values('table__number').annotate(total=Count('id')).order_by('table__number')
    return render(request, 'bookings/booking_analytics.html', {'table_data': table_data})


@staff_member_required
def table_analytics(request):
    table_stats = Booking.objects.values('table__number').annotate(total=Count('id')).order_by('-total')
    return render(request, 'bookings/table_analytics.html', {'table_stats': table_stats})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
