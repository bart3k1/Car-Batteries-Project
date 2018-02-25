from django.http import HttpResponse
from django.shortcuts import render, redirect
from pojazdy.models import Pojazdy, Baterie#, Dane
from django.views import View

# Create your views here.

class PojazdyDetails(View):
    def get(self, request):
        pojazd = Pojazdy.objects.get(id=4)
        # dane = Dane.objects.all()
        counter = 0
        baterie = pojazd.bateries.all()
        for i in baterie:
            counter += 1
        return render(request, 'pojazdy_details.html', {
            'pojazd': pojazd,
            'baterie': baterie,
            'counter': counter,

        })

    def post(self, request):
        self.name = request.POST['name']
        self.surname = request.POST['surname']
        self.phone = request.POST['phone']
        self.notes = request.POST['notes']
        guest = Guests.objects.create(name=self.name, surname=self.surname, phone=self.phone, notes=self.notes)
        guest.save()
        guests = Guests.objects.all()
        return render(request, 'guests_details.html', {
            'guests': guests
        })

class NowyPojazd(View):
    def get(self, request):
        return render(request, 'nowy_pojazd.html', {
        })
    def post(self, request):
        self.userID = request.POST['userID']
        self.nazwa = request.POST['nazwa']
        self.baterie = request.POST['baterie']
        p = Pojazdy.objects.create(userID=self.userID, nazwa=self.nazwa)
        counter = 1
        counterID = 5
        for _ in range(int(self.baterie)):
            b = Baterie.objects.create(numer=counter, batID=counterID)
            b.save()
            p.bateries.add(b)
            counter += 1
            counterID += 2
        return redirect("/pojazdy")