from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display=(
        'author','title','created_at','is_public'
    )

admin.site.register(Article,ArticleAdmin)