from django.contrib import admin
from .models import Editor, Tag, Article

# Customize models
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

# Create Admin Model Objects
admin.site.register(Editor)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
