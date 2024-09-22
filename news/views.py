from django.contrib.auth.models import User
from .models import News as ModelNews
from django.views.generic import ListView, DetailView
from blog.models import PostBlog
from authors.models import Authors


# Create your views here.

class News(ListView):
    model = ModelNews
    context_object_name = 'posts'
    template_name = 'news/index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-id')

        return qs[0:8]

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)

        first_news = ModelNews.objects.filter(type_news__type_news='M').order_by('-id').first()
        second_news = ModelNews.objects.filter(type_news__type_news='S').order_by('-id').first()
        third_news = ModelNews.objects.filter(type_news__type_news='T').order_by('-id').first()
        posts_blog = PostBlog.objects.filter(is_published=True).order_by('-id')[0:5]

        new_users = Authors.objects.filter(is_active=True).order_by('-id')[0:5]

        cd.update({
            'five_users': new_users,
            'first_news': first_news,
            'second_news': second_news,
            'third_news': third_news,
            'posts_blog': posts_blog
        })

        return cd


class ReadNews(DetailView):
    template_name = 'news/read_news.html'
    context_object_name = 'post'
    model = ModelNews

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(slug=self.kwargs.get('slug'))

        return qs

    def get_context_data(self, **kwargs):
        cd = super().get_context_data(**kwargs)

        last_posts = ModelNews.objects.all().filter(is_published=True).exclude(slug=self.kwargs.get('slug'))[0:5]

        cd['last_posts'] = last_posts

        return cd


class AllNews(ListView):
    model = ModelNews
    paginate_by = 1
    context_object_name = 'posts'
    template_name = 'global/partials/all_posts.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_published=True).order_by('-id')

        return qs
