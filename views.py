from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

def home(request):
    return render(request, 'customer/home.html')



def news(request):
        return render(request, 'customer/news.html')

def about(request):
    return render(request, 'customer/about.html')

def csr(request):
    return render(request, 'customer/csr.html')

def sustain(request):
    return render(request, 'customer/sustain.html')

# def sighnup(request):

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = CustomerRegistration(name=name, email=email, password=password)
#         customer.save()
#         return redirect('customer:login') 

#     return render(request, 'Customer/sighnup.html')

# from django.shortcuts import render, redirect
# from .models import CustomerRegistration

# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         cust = CustomerRegistration.objects.filter(name=name, email=email, password=password).first()

#         if cust:
#             request.session['customer'] = cust.id
#             return redirect('customer:home')

#         else:
#             return render(request, 'customer/login.html', {'error': 'Invalid credentials'})

#     return render(request, 'customer/login.html')

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import CustomerRegistration

# def sighnup(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Prevent duplicate email signup
#         if CustomerRegistration.objects.filter(email=email).exists():
#             return render(request, 'customer/sighnup.html', {'error': 'Email already registered!'})

#         customer = CustomerRegistration(name=name, email=email, password=password)
#         customer.save()
#         return redirect('customer:login')

#     return render(request, 'customer/sighnup.html')

from django.shortcuts import render, redirect
from .models import CustomerRegistration

def sighnup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Prevent duplicate email registration
        if CustomerRegistration.objects.filter(email=email).exists():
            return render(request, 'customer/sighnup.html', {'error': 'Email already registered!'})

        # Save the new customer in database
        customer = CustomerRegistration(name=name, email=email, password=password)
        customer.save()
        return redirect('customer:login')  # redirect to login after signup

    return render(request, 'customer/sighnup.html')



# def login(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         cust = CustomerRegistration.objects.filter(name=name, email=email, password=password).first()

#         if cust:
#             request.session['customer'] = cust.id
#             return redirect('customer:home')
#         else:
#             return render(request, 'customer/login.html', {'error': 'Invalid credentials'})

#     return render(request, 'customer/login.html')


# def home(request):
#     return render(request, 'customer/home.html')

from django.shortcuts import render, redirect
from .models import CustomerRegistration

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        cust = CustomerRegistration.objects.filter(
            name=name, email=email, password=password
        ).first()

        if cust:
            request.session['customer'] = cust.id
            return redirect('customer:home')
        else:
            return render(request, 'customer/login.html', {'error': 'Invalid credentials'})

    return render(request, 'customer/login.html')



from django.shortcuts import render
from .models import GasBooking

def book_gas(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        confirmation_code = request.POST.get('confirmation_code')

        # Save to DB
        GasBooking.objects.create(
            name=name,
            phone=phone,
            address=address,
            confirmation_code=confirmation_code
        )
        success_message = "Thank you, your HP Gas booking is confirmed!."

    return render(request, 'customer/book_gas.html', {'success_message': success_message})

