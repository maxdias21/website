from django.forms import ModelForm
from ..models import Authors


class Profile(ModelForm):
    class Meta:
        model = Authors
        fields = '__all__'
        exclude = ['slug', 'username', 'is_active']
        labels = {
            'age': 'Idade',
            'hometown': 'Em qual estado você nasceu?',
            'current_city': 'Em qual estado você mora?',
            'sex': 'Como você se identifica? (Masculino/Feminino/Outro)',
            'marital_status': 'Qual é o seu estado civil? (Casado(a)/Solteiro(a)/Divorciado(a)/Viúvo(a))',
            'profile_status': 'Seu perfil vai ser público ou privado?',
            'profile_photo': 'Foto do Perfil',
            'description': 'Descrição do Perfil'
        }
        help_texts = {
            'profile_status': 'Se o seu perfil for privado, ninguém poderá acessá-lo, mas seus posts continuarão visíveis para todos na comunidade! 😊'
        }
