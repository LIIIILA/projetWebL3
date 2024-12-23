from django.shortcuts import render, get_object_or_404
from .models import Box, Reservation
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def make_reservation(request, box_id):
    box = get_object_or_404(Box, id=box_id)
    if request.method == 'POST':
        # Traitement de la réservation ici
        pass
    return render(request, 'reservations/make_reservation.html', {'box': box})
