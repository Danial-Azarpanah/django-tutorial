from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View

from.models import Article, Comment, Category


# class BlogDetail(DetailView):
#     model = Article
#     template_name = "post/detail.html"
class BlogDetail(View):
    def get(self, request, slug):
        object = get_object_or_404(Article, slug=slug)
        return render(request, "post/detail.html", {"object": object})
    
    def post(self, request, slug):
        Comment.objects.create(
            user=request.user,
            article_id=request.POST.get("article-id"),
            body=request.POST.get("message"),
        )
        return redirect("blog-detail", slug=slug)


class BlogList(View):
    def get(self, request):
        articles = Article.objects.select_related("author").prefetch_related("comments").order_by("-created_at")
        q = request.GET.get("q")
        if q:
            articles = articles.filter(title__icontains=q)
        top_3_articles = Article.objects.order_by("-view_count")[:3]
        categories = Category.objects.all()
        return render(request, "post/list.html", {
            "articles": articles,
            "top_articles": top_3_articles, 
            "categories": categories}
            )


class CommentDelete(View):
    def get(self, request, id):
        object = get_object_or_404(Comment, id=id)
        article_slug = object.article.slug
        object.delete()
        return redirect("blog-detail", slug=article_slug)
