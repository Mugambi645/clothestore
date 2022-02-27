from .models import ContactUs
from django import forms

from django.forms import ModelForm
class ContactForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'