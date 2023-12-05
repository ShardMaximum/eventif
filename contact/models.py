from django.core import mail
from django.db import models


class Message(models.Model):
    name = models.CharField('nome', max_length=200)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20, blank=True)
    message = models.CharField('mensagem', max_length=2000)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    response = models.CharField('mensagem', max_length=2000)
    response_date = models.DateTimeField('respondido em')

    class Meta:
        verbose_name = "mensagem"
        verbose_name_plural = "mensagens"
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.message