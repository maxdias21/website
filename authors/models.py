from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Authors(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=False, verbose_name=_('Username'))
    age = models.IntegerField(validators=[MinValueValidator(0)], verbose_name=_('Age'))
    hometown = models.CharField(choices=(
        ('Acre', 'Acre'),
        ('Alagoas', 'Alagoas'),
        ('Amapá', 'Amapá'),
        ('Amazonas', 'Amazonas'),
        ('Bahia', 'Bahia'),
        ('Ceará', 'Ceará'),
        ('Distrito Federal', 'Distrito Federal'),
        ('Espírito Santo', 'Espírito Santo'),
        ('Goiás', 'Goiás'),
        ('Maranhão', 'Maranhão'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
        ('Minas Gerais', 'Minas Gerais'),
        ('Pará ', 'Pará '),
        ('Paraíba', 'Paraíba'),
        ('Paraná', 'Paraná'),
        ('Pernambuco', 'Pernambuco'),
        ('Piauí', 'Piauí'),
        ('Rio de Janeiro', 'Rio de Janeiro'),
        ('Rio Grande do Norte', 'Rio Grande do Norte'),
        ('Rio Grande do Sul', 'Rio Grande do Sul'),
        ('Rondônia', 'Rondônia'),
        ('Roraima', 'Roraima'),
        ('Santa Catarina', 'Santa Catarina'),
        ('São Paulo', 'São Paulo'),
        ('Sergipe', 'Sergipe'),
        ('Tocantins', 'Tocantins'),
    ), max_length=19, default='', null=False, blank=False, verbose_name=_('Hometown'))
    current_city = models.CharField(choices=(
        ('Acre', 'Acre'),
        ('Alagoas', 'Alagoas'),
        ('Amapá', 'Amapá'),
        ('Amazonas', 'Amazonas'),
        ('Bahia', 'Bahia'),
        ('Ceará', 'Ceará'),
        ('Distrito Federal', 'Distrito Federal'),
        ('Espírito Santo', 'Espírito Santo'),
        ('Goiás', 'Goiás'),
        ('Maranhão', 'Maranhão'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso', 'Mato Grosso'),
        ('Mato Grosso do Sul', 'Mato Grosso do Sul'),
        ('Minas Gerais', 'Minas Gerais'),
        ('Pará ', 'Pará '),
        ('Paraíba', 'Paraíba'),
        ('Paraná', 'Paraná'),
        ('Pernambuco', 'Pernambuco'),
        ('Piauí', 'Piauí'),
        ('Rio de Janeiro', 'Rio de Janeiro'),
        ('Rio Grande do Norte', 'Rio Grande do Norte'),
        ('Rio Grande do Sul', 'Rio Grande do Sul'),
        ('Rondônia', 'Rondônia'),
        ('Roraima', 'Roraima'),
        ('Santa Catarina', 'Santa Catarina'),
        ('São Paulo', 'São Paulo'),
        ('Sergipe', 'Sergipe'),
        ('Tocantins', 'Tocantins'),
    ), max_length=19, default='', null=False, blank=False, verbose_name=_('Current City'))
    sex = models.CharField(choices=(('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')), max_length=10, verbose_name=_('Sex'))
    marital_status = models.CharField(choices=(('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')),
                                      max_length=10, verbose_name=_('Current City'))
    description = models.TextField(verbose_name=_('Description'))
    profile_status = models.CharField(choices=(('Público', 'Público'), ('Privado', 'Privado')), max_length=10,
                                      verbose_name=_('Profile Status'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_('Updated at'))
    slug = models.SlugField(unique=True, max_length=255, blank=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='profile/photo_profile',
                                      verbose_name=_('Profile Photo'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _('Authors')
        verbose_name = _('Authors')

    def __str__(self):
        return str(self.username)
