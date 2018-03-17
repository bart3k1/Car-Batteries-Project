from django import forms
from django.core.validators import validate_email, URLValidator
from .models import Pojazdy, Baterie


class PojazdyForm(forms.Form):
    userID = forms.CharField(max_length=64)
    nazwa = forms.CharField(max_length=50)
    baterie = forms.IntegerField()


class EditPojazdyForm(forms.Form):
    def __init__(self, pojazd_id, *args, **kwargs):
        super(EditPojazdyForm, self).__init__(*args, **kwargs)
        self.pojazd_id = pojazd_id
        self.userID = forms.CharField(max_length=64)
        self.nazwa = forms.CharField(max_length=50)
        self.baterie = forms.IntegerField()
        self.baterie_on = forms.ModelMultipleChoiceField(
            queryset=Baterie.objects.all().filter(inpojazd_id=self.pojazd_id),
            widget=forms.CheckboxSelectMultiple,
            )

    class Meta:
        model = Pojazdy

