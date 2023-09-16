from django.contrib import messages
from django.conf import settings
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from contact.forms import ContactForm

def show_contact_form(request):
    return render(request, 'contact_form.html', {'form': ContactForm})

def send_msg(request):
    form = ContactForm(request.POST)
    if not form.is_valid():
        return render(request, 'contact_form.html', {'form': form})
    
    mailbody = render_to_string('contact_email.txt', form.cleaned_data)
    sender = settings.DEFAULT_FROM_MAIL
    mail.send_mail('Mensagem enviada através do site',
                   mailbody,
                   sender,
                   [sender, form.cleaned_data['email']])

    messages.success(request, "Um email foi enviado para nossa equipe. Obrigado!")
    return HttpResponseRedirect('/contato/')

def contact(request):
    if request.method == 'POST':
        return send_msg(request)
    else:
        return show_contact_form(request)