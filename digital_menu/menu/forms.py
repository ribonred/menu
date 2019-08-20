from django import forms
from django.forms import widgets
from .models import Order

pilih_jumlah = [(i, str(i)) for i in range(1,11)]

class formtambahproduk(forms.Form):
    quantity = forms.TypedMultipleChoiceField(choices=pilih_jumlah,coerce=int)
    update = forms.BooleanField(required=False, initial=False,widget=forms.HiddenInput)
class formupdateproduk(forms.Form):
    quantity = forms.DecimalField()
class orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nama', 'no_tlp']