from django.shortcuts import render
from contact.forms import ContactForm

def show_contact_form(request):
    return render(request, 'contact_form.html', {'form': ContactForm})

def send_msg(request):
    
    pass