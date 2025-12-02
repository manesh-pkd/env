from django.db import models

# class CustomerRegistration(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

from django.db import models

class CustomerRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class GasBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    confirmation_code = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"


from django.db import models

class CustomerRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
