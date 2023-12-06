from django.core import mail
from django.test import TestCase
from contact.models import Message

class ContactModelTest(TestCase):
    def setUp(self):
        self.message = Message.objects.create(
            name = 'Vitor Rocha',
            email = 'vitor.rocha@aluno.riogrande.ifrs.edu.br',
            phone = '53-91234-5678',
            message = 'Mensagem de teste'
        )
        self.message.save()

    def test_created(self):
        self.assertTrue(Message.objects.exists())

    def test_str(self):
        self.assertEqual('Mensagem de teste', str(self.message))

    def test_send_mail_on_response(self):
        self.message.response = 'Teste de resposta.'
        self.message.save()
        self.assertEqual(1, len(mail.outbox))