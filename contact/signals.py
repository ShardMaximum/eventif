from datetime import datetime
from django.db.models.signals import post_save

def send_mail_answer(sender, instance, created, **kwargs):
    if not created:
        if "response" in kwargs.get("update_fields"):
            instance.update('response_date':datetime.now())
            subject = "Resposta da equipe do eventif"
            mailfrom = "contato@eventif.combr"
            mailto = instance.email
            mailbody = render_to_string('contact_response.txt', instance)
            mail.send_mail(subject, mailbody, mailfrom, [mailfrom, mailto])


post_save.connect(send_mail_answer, sender=Message)