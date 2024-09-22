from django.views import View
from django.shortcuts import redirect
from ..models import Authors
from ..forms.profile import Profile
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IsLogged(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('authors:my_profile')

        return super().dispatch(request, *args, **kwargs)

class BaseAuthorHasNotPerfil(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.profile = None

        if (self.request.user.is_authenticated):
            self.profile = Authors.objects.filter(username=self.request.user).exists()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(
                request=request,
                message='Crie uma conta para acessar informações exclusivas do nosso site! É grátis 😊')
            return redirect('authors:register')

        if self.profile:
            messages.info(request, 'Parece que você ainda não possui um perfil. Vamos criar um agora!')
            return redirect('authors:my_account')


        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required(login_url='authors:register'), name='dispatch')
class BasePerfilHasAuthor(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        if (self.request.user.is_authenticated):
            self.profile = Authors.objects.filter(username=self.request.user).first()
        else:
            messages.info(
                request=request,
                message='Crie uma conta para acessar informações exclusivas do nosso site! É grátis 😊')
            return

        self.form = Profile(
            data=request.POST or None,
            instance=self.profile,
            files=request.FILES or None)

    def dispatch(self, request, *args, **kwargs):
        if not self.profile:
            messages.info(request, 'Parece que você ainda não possui um perfil. Vamos criar um agora!')
            return redirect('authors:create_profile')

        return super().dispatch(request, *args, **kwargs)
