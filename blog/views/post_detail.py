from django.views.generic import DetailView
from ..models import PostBlog


class ReadPost(DetailView):
    model = PostBlog
    context_object_name = 'post'
    template_name = 'blog/read_post.html'

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)

        last_posts = PostBlog.objects.all().filter(is_published=True).exclude(slug=self.kwargs.get('slug'))[0:4]
        cd['last_posts'] = last_posts

        return cd
