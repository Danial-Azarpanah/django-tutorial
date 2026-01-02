from django.shortcuts import render
from django.views import View

from post.models import Article


class Home(View):
    def get(self, request):
        first_3_articles = Article.objects.all()[:3]
        popular_articles = Article.objects.order_by("-view_count")
        context = {
            "articles": first_3_articles,
            "popular_articles": popular_articles,
        }
        return render(request, "home/home.html", context)


def home(request):
    if request.method == "GET":
        first_3_articles = Article.objects.all()[:3]
        popular_articles = Article.objects.order_by("-view_count")
        context = {
            "articles": first_3_articles,
            "popular_articles": popular_articles,
        }
        return render(request, "home/home.html", context)
