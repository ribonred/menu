from django import forms
from django.forms import widgets

pilih_jumlah = [(i, str(i)) for i in range(1,11)]

class formtambahproduk(forms.Form):
    quantity = forms.TypedMultipleChoiceField(choices=pilih_jumlah,coerce=int)
    update = forms.BooleanField(required=False, initial=False,widget=forms.HiddenInput)
