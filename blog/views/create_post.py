from django.shortcuts import render, redirect, reverse
from ..forms.add_post import AddPost
from authors.views.base_profile import BasePerfilHasAuthor
from django.contrib import messages


class CreatePost(BasePerfilHasAuthor):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('authors:login')

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form_session = request.session.get('create_post_session', None)

        form = AddPost(form_session)

        return render(request, 'blog/create_post.html', {
            'form': form,
            'title': 'Crie e publique seu post já!'
        })

    def post(self, request):
        form_action_url = reverse('blog:create_post')

        post = self.request.POST

        self.request.session['create_post_session'] = post

        form = AddPost(post)

        if form.is_valid():
            user = form.save(commit=False)

            user.author = self.request.user
            user.save()

            messages.success(
                request=request,
                message='🌟 Seu post foi criado com sucesso e agora está em processo de avaliação! Agradecemos por contribuir e compartilhar suas ideias.')

            del request.session['create_post_session']
            return redirect('authors:my_profile')

        messages.error(
            request=request,
            message='Erro ao criar o seu post. Por favor, verifique se todos os campos estão preenchidos corretamente.')

        return render(request, template_name='blog/create_post.html', context={
            'form': form,
            'form_action_url': form_action_url
        })
