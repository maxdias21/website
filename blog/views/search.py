from django.views.generic import ListView
from ..models import PostBlog
from django.db.models import Q
from authors.models import Authors
from news.models import News


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    model = PostBlog

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.search_term = request.GET.get('q', '')

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(Q(title__icontains=self.search_term) | Q(description__icontains=self.search_term),
                       is_published=True).order_by('-id')

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        cd = super().get_context_data(**kwargs)

        users = Authors.objects.filter(
            Q(username__first_name__icontains=self.search_term) | Q(username__username__icontains=self.search_term))
        print(users)

        cd['users'] = users

        news = News.objects.filter(Q(title__icontains=self.search_term) | Q(description__icontains=self.search_term),
                                   is_published=True).order_by('-id')

        cd['news'] = news

        cd['search_term'] = self.search_term

        return cd
