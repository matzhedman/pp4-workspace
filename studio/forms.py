from django import forms
from django.forms import ModelForm
from .models import Offer


# datepicker
class DateInput(forms.DateInput):
    input_type = 'date'


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = fields = '__all__'
        widgets = {
            'expiration_date': DateInput(),
        }


class UserForm(forms.Form):
    first_name = forms.CharField(max_length = 35)
    last_name = forms.Charfield(max_length = 35)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 500)
