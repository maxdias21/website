from django.shortcuts import redirect
from django.views.generic import DetailView
from ..models import Authors
from django.contrib import messages
from blog.models import PostBlog


class UserProfile(DetailView):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.profile = Authors.objects.all().filter(slug=kwargs.get('slug'), is_active=False).first()

        if not self.profile:
            self.profile = Authors.objects.all().filter(slug=kwargs.get('slug'), profile_status='Privado')

    def dispatch(self, request, *args, **kwargs):
        if self.profile:
            messages.error(request, 'O perfil é privado ou não existe!')
            return redirect('blog:all_users')

        return super().dispatch(request, *args, **kwargs)

    model = Authors
    template_name = 'authors/user-profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)

        author = Authors.objects.filter(slug=self.kwargs.get('slug')).first()
        user_posts = PostBlog.objects.filter(author=author.username, is_published=True)
        cd['posts'] = user_posts

        return cd
