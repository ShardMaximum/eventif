from django import forms
from contact.models import Message

class ContactForm(forms.Form):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'message']