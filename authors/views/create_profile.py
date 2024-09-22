from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from ..forms.profile import Profile
from .base_profile import BaseAuthorHasNotPerfil

class CreateProfile(BaseAuthorHasNotPerfil):

    def get(self, request):
        create_profile_form_data = self.request.session.get('create_profile_form_data', None)

        form = Profile(create_profile_form_data)

        return render(request=request, template_name='authors/create_profile.html', context={
            'form': form,
            'title': 'Crie seu perfil e junte-se à nossa comunidade!'
        })

    def post(self, request):
        form_action_url = reverse('authors:create_profile')

        post = self.request.POST

        self.request.session['create_profile_form_data'] = post

        form = Profile(post)

        if form.is_valid():
            user = form.save(commit=False)

            user.username = request.user
            user.save()

            messages.success(
                request=request,
                message='Seu perfil foi criado com sucesso!')

            del request.session['create_profile_form_data']
            return redirect('authors:my_profile')

        messages.error(
            request=request,
            message='Erro ao editar o seu perfil. Por favor, verifique se todos os campos estão preenchidos corretamente.')

        return render(request, template_name='authors/my_profile.html', context={
            'form': form,
            'form_action_url': form_action_url,
        })
