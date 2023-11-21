from django import forms
from phonenumber_field.formfields import PhoneNumberField


class MyForm(forms.Form):
    email = forms.EmailField()
    phone = PhoneNumberField(region="RU")
    date = forms.DateField(required=True)
    text = forms.CharField(required=False)

