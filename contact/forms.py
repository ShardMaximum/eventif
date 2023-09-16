from django import forms

class ContactForm(forms.form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone', blank=True)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)