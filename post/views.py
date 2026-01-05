from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, View

from.models import Article


# class BlogDetail(DetailView):
#     model = Article
#     template_name = "post/detail.html"
class BlogDetail(View):
    def get(self, request, slug):
        object = get_object_or_404(Article, slug=slug)
        return render(request, "post/detail.html", {"object": object})
