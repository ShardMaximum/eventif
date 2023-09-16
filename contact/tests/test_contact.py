from django.core import mail
from django.test import TestCase

from contact.forms import ContactForm

class ContactTest(TestCase):
    def setUp(self):
        data = dict(name = 'Vitor Rocha',
                    email = 'vitor.rocha@aluno.riogrande.ifrs.edu.br',
                    phone = '53-91234-5678',
                    message = 'Mensagem de teste')

    def test_get(self):
        self.response = self.client.get('/contato/')
        self.assertEqual(200, self.response.status_code)

    def test_post(self):
        self.response = self.client.post('/contato/', self.data)
        self.assertEqual(302, self.response.status_code)

    def test_post_wrong(self):
        self.response = self.client.post('/inscricao/',{})
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_mail_sent(self):
        self.response = self.client.post('/contato/', self.data)
        self.assertEqual(1, len(mail.outbox))