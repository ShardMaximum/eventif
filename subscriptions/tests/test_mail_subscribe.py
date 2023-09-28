from django.test import TestCase
from django.core import mail

class MailTest(TestCase):
    def setUp(self):
        data = dict(name="Vitor Rocha", 
                    cpf="12345678901", 
                    email="vitor.rocha@aluno.riogrande.ifrs.edu.br", 
                    phone="53912345678")
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = "vitor.rocha@aluno.riogrande.ifrs.edu.br"
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['vitor.rocha@aluno.riogrande.ifrs.edu.br', 'vitor.rocha@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Vitor Rocha',
                    '12345678901',
                    'vitor.rocha@aluno.riogrande.ifrs.edu.br',
                    '53-91234-5678']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)