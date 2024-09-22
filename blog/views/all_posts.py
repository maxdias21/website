from django.views.generic import ListView
from ..models import PostBlog


class ListPosts(ListView):
    model = PostBlog
    context_object_name = 'posts'
    template_name = 'global/partials/all_posts.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-id')

        return qs
