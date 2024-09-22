from .base_profile import BasePerfilHasAuthor
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from blog.models import PostBlog
from blog.forms.add_post import AddPost


class MyProfile(BasePerfilHasAuthor):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

    def get(self, request):
        posts = PostBlog.objects.filter(author=self.profile.username, is_published=True)

        return render(
            request=request,
            template_name='authors/my_profile.html',
            context={
                'form': self.form,
                'profile': self.profile,
                'title': 'Atualize suas informações para que possamos oferecer uma experiência personalizada. Certifique-se de que seus dados estão sempre atualizados!',
                'posts': posts,
            })

    def post(self, request):
        form_action_url = reverse('authors:my_profile')

        # Verifica se o formulário de edição de perfil foi submetido
        if 'form_edit_user' in request.POST:
            if self.form.is_valid():
                form = self.form.save(commit=False)
                form.username = request.user  # Associa o perfil ao usuário
                form.save()

                messages.success(
                    request=request,
                    message='Seu perfil foi editado com sucesso!')

                return redirect('authors:my_profile')

            messages.error(
                request=request,
                message='Erro ao editar o seu perfil. Por favor, verifique se todos os campos estão preenchidos corretamente.')


        # Renderiza a página novamente em caso de erro
        return render(request, template_name='authors/my_profile.html',
                      context={
                          'form': self.form,
                          'form_add_post': AddPost(),
                          'form_action_url': form_action_url
                      })
