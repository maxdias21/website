from django.shortcuts import render, redirect
from authors.forms.register import RegisterForm
from django.views import View
from django.contrib import messages


class Register(View):
    def get(self, request):
        register_form_data = self.request.session.get('register_form_data', None)

        form = RegisterForm(register_form_data)

        return render(
            request=request,
            template_name='authors/register.html',
            context={
                'form': form,
                'title': 'Crie sua conta para começar a explorar nosso conteúdo! É rápido, fácil e gratuito 😊'
            })

    def post(self, request):
        post = self.request.POST

        self.request.session['register_form_data'] = post

        form = RegisterForm(post)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            messages.success(
                request=request,
                message='Sua conta foi criada com sucesso!')

            del request.session['register_form_data']
            return redirect('authors:login')

        messages.error(
            request=request,
            message='Erro ao criar sua conta. Por favor, verifique se todos os campos estão preenchidos corretamente.')

        return render(request, template_name='authors/register.html', context={'form': form})
