from django.contrib import messages
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .base_profile import IsLogged

class Login(IsLogged):
    def get(self, request):
        return render(
            request=request,
            template_name='authors/login.html',
        )

    def post(self, request):
        username_field = request.POST.get('username')
        password_field = request.POST.get('password')

        authenticate_user = authenticate(username=username_field, password=password_field)

        if (authenticate_user):
            messages.success(
                request=request,
                message=f'Olá, {username_field}! Você fez login com sucesso!')

            login(request=self.request, user=authenticate_user)

            return redirect('authors:my_profile')

        messages.error(
            request=request,
            message='Seu usuário ou senha estão incorretos, tente novamente!')

        return render(request=request,
                      template_name='authors/login.html',
                      context={
                          'username': username_field,
                          'password': password_field
                      }
                      )
