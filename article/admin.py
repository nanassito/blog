from article.models import Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
    )
    
    search_fields = (
        'title',
        'date',
        'content'
    )

admin.site.register(Article, ArticleAdmin)
