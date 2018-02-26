from django.http import HttpResponse
from django.shortcuts import render, redirect
from pojazdy.models import Pojazdy, Baterie#, Dane
from django.views import View

# Create your views here.

class PojazdyDetails(View):
    def get(self, request):
        pojazdy = Pojazdy.objects.all()
        return render(request, 'pojazdy_details.html', {
            'pojazdy': pojazdy,
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
            b.inpojazd = p
            b.save()
            counter += 1
            counterID += 2
        return redirect("/pojazdy")


class EdytujPojazd(View):
    def get(self, request, pojazd_id):
        pojazd = Pojazdy.objects.get(id=pojazd_id)
        pojazdy = Pojazdy.objects.all()
        baterieAll = len(pojazd.baterie.all())
        print(baterieAll)
        baterieON = len(pojazd.baterie.filter(on=True))
        print(baterieON)
        return render(request, 'edytuj_pojazd.html', {
            'pojazdy': pojazdy,
            'pojazd': pojazd,
            'baterieON': baterieON,
            'baterieAll': baterieAll,

           })
    def post(self, request, pojazd_id):
        p = Pojazdy.objects.get(id=pojazd_id)
        self.userID = request.POST['userID']
        self.nazwa = request.POST['nazwa']
        #dodawanie baterii i usuwanie baterii zrobic!
        self.baterie = request.POST['baterie']
        # jesli sa - to countery sie zmieniaja
        counter = 1
        counterID = 5
        for _ in range(int(self.baterie)):
            b = Baterie.objects.create(numer=counter, batID=counterID)
            b.inpojazd = p
            b.save()
            counter += 1
            counterID += 2
        return redirect("/pojazdy")

