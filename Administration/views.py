from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from Reservation.models import Reservations

def admin_dashboard(request):
    reservations = Reservations.objects.all()
    return render(request, 'Administration/dashboard.html', {'reservations': reservations})
