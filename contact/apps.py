from django.apps import AppConfig

class ContactConfig(AppConfig):
    name = "contact"
    verbose_name = "Contato com a equipe"

    def ready(self):
        import contact.signals