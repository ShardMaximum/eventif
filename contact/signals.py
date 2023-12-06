from datetime import datetime
from django.core import mail
from django.db.models.signals import post_save

from contact.models import Message

def send_mail_answer(sender, instance, created, update_fields, **kwargs):
    if not created and "response" in update_fields:
        instance.response_date = datetime.now()
        subject = "Resposta da equipe do eventif"
        mailfrom = "contato@eventif.combr"
        mailto = instance.email
        mailbody = render_to_string('contact_response.txt', instance)
        mail.send_mail(subject, mailbody, mailfrom, [mailfrom, mailto])


post_save.connect(send_mail_answer, sender=Message)