from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField

# Validators
from django.core.validators import ValidationError
from utils.validators.validators import validate_min_length_multiple


class RegisterForm(ModelForm):
    repeat_password = forms.CharField(required=True, max_length=128, min_length=8, label='Confirmar Senha',
                                      widget=forms.PasswordInput())
    captcha = CaptchaField(label='Verificação de segurança',
                           help_text='Esta verificação ajuda a evitar envios automáticos e manter o site seguro.',
                           )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': 'Senha'
        }

        widgets = {
            'username': forms.TextInput(attrs={'max_length': '50', 'placeholder': 'Usuário'}),
            'first_name': forms.TextInput(attrs={'first_name': '255', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'max_length': '255', 'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'max_length': '255', 'placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'max_length': '128'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        username_exists = User.objects.filter(username=username).exists()

        if username_exists:
            raise ValidationError('Usuário já cadastrado', code='invalid')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise ValidationError('Este e-mail já está cadastrado. Por favor, tente outro.', code='invalid')

        return email

    def clean(self):
        cleaned_data = super().clean()
        min_length = 6

        first_name_input = cleaned_data.get('first_name')
        last_name_input = cleaned_data.get('last_name')
        password_input = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password_input != repeat_password:
            raise ValidationError({
                'password': 'Senhas precisam ser iguais',
                'repeat_password': 'Senhas precisam ser iguais'
            })

        errors = validate_min_length_multiple([
            {'first_name': {
                'field': first_name_input,
                'field_name': 'nome',
                'error_message': f'O campo nome não pode ter menos que {min_length} caracteres'
            }},
            {'last_name': {
                'field': last_name_input,
                'field_name': 'sobrenome',
                'error_message': f'O campo sobrenome não pode ter menos que {min_length} caracteres'
            }}
        ], min_length)

        if not errors:
            raise ValidationError(errors)
