from django.core import mail
from django.db import models
from django.db.models.signals import post_save

class Message(models.Model):
    name = models.CharField('nome', max_length=200)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20, blank=True)
    message = models.CharField('mensagem', max_length=2000)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    response = models.CharField('mensagem', max_length=2000)
    response_date = models.DateTimeField('respondido em', auto_now_add=True)
    answered = models.BooleanField('respondido', default=False)

    class Meta:
        verbose_name = "mensagem"
        verbose_name_plural = "mensagens"
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.message

    def send_mail_answer(sender, instance, **kwargs):
        mailbody = render_to_string('contact_response.txt', instance)
        mail.send_mail()