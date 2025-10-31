from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.capacity} seats)"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Table {self.table.number} at {self.booking_time}"
from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - Table {self.table_number} on {self.booking_date} at {self.booking_time}"
