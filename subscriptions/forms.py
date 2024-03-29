from django import forms
from django.core.exceptions import ValidationError
from subscriptions.models import Subscription
from subscriptions.validators import validate_cpf

class SubscriptionForm(forms.ModelForm):
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu email ou telefone')