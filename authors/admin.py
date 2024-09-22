from django.contrib import admin
from .models import Authors


# Register your models here.

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_active')
    list_editable = ('is_active',)
    list_per_page = 10
    list_display_links = ('id', 'username')


admin.site.register(Authors, AuthorsAdmin)
