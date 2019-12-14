from django.contrib import admin

from .models import Article, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0 # No extra comment fields in admin

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)