from django.contrib import admin

from .models import Article, Category, Comment


# admin.site.register(Article)


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "get_body", "created_at"]
    search_fields = ["title"]
    list_filter = ["created_at", "is_published"]
    inlines = [CommentInline]
    prepopulated_fields = {"slug": ("title",)} 

    def get_body(self, obj):
        if len(obj.body) > 30:
            return obj.body[:30] + " ..."
        return obj.body
    get_body.short_description = "بدنه"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} 


