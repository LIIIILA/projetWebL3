document.addEventListener('DOMContentLoaded', function () {
    const reservationForm = document.getElementById('reservation-form');

    reservationForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Empêche le formulaire de soumettre normalement

        // Récupérer les données du formulaire
        const box = document.getElementById('box').value;
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;

        // Créer un objet pour la réservation
        const reservation = {
            box: box,
            date: date,
            time: time
        };

        // Récupérer l'historique existant ou créer un tableau vide
        let historyList = JSON.parse(localStorage.getItem('reservations')) || [];

        // Ajouter la nouvelle réservation à l'historique
        historyList.push(reservation);

        // Sauvegarder à nouveau l'historique dans le localStorage
        localStorage.setItem('reservations', JSON.stringify(historyList));

        // Optionnellement, afficher un message de confirmation ou réinitialiser le formulaire
        alert('Réservation effectuée avec succès !');
        reservationForm.reset(); // Réinitialise le formulaire après soumission
    });
});
