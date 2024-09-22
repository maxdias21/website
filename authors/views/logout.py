from django.views import View
from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

class Logout(View):
    def get(self, request):
        messages.error(request, 'Houve um erro ao sair da sua conta!')
        return redirect('authors:my_profile')

    def post(self, request):
        if request.POST.get('username') != request.user.username:
            messages.error(request, 'Ocorreu um erro ao tentar sair da conta. Por favor, tente novamente.')
            return redirect('authors:my_profile')

        messages.success(request, 'Você saiu da sua conta com sucesso!')
        logout(request)
        return redirect('authors:login')