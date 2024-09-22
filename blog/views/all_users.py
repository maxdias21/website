from django.views.generic import ListView
from authors.models import Authors

class ListUsers(ListView):
    model = Authors
    template_name = 'blog/all_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = super().get_queryset()

        filter = qs = qs.filter(is_active=True)

        return filter
