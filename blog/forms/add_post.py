from blog.models import PostBlog
from django.forms import ModelForm
from captcha.fields import CaptchaField


class AddPost(ModelForm):
    captcha = CaptchaField(label='Verificação de segurança', help_text='Esta verificação ajuda a evitar envios automáticos e manter o site seguro.')

    class Meta:
        model = PostBlog
        fields = '__all__'
        exclude = ['slug', 'is_published', 'author']
        labels = {
            'title': 'Título do seu post',
            'description': 'Descrição do seu post',
            'content': 'Conteúdo do seu post',
            'imagem': 'Imagem do post'
        }
