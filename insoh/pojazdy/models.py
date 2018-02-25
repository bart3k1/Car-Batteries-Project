from django.db import models

# Create your models here.


class Pojazdy(models.Model):
    userID = models.CharField(max_length=64, unique=True, null=False)
    nazwa = models.CharField(max_length=50, null=False)


class Baterie(models.Model):
    nazwa = models.CharField(max_length=50, null=True)
    numer = models.IntegerField(null=True)
    batID = models.IntegerField(null=True)
    on = models.BooleanField(default=True)
    inpojazd = models.ForeignKey(Pojazdy,  null=True, related_name="baterie", on_delete=models.CASCADE)


# class Dane(models.Model):
#     pojazd = models.ForeignKey(Pojazdy, on_delete=models.CASCADE)
#     bateria = models.ForeignKey(Baterie, on_delete=models.CASCADE)
#     numer = models.IntegerField(null=True)
#     batID = models.IntegerField(null=True)
#     on = models.BooleanField(default=True)
#     # ilosc = models.IntegerField(null=True)
#     # niepotrzebna bo mozna zliczyc po id auta