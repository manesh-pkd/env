from django.contrib import admin

from .models import GasBooking

@admin.register(GasBooking)
class GasBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'confirmation_code', 'booking_date')

from django.contrib import admin
from .models import CustomerRegistration

@admin.register(CustomerRegistration)
class CustomerRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


