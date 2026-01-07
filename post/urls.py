from django.urls import path

from . import views


urlpatterns = [
    path("detail/<str:slug>/", views.BlogDetail.as_view(), name='blog-detail'),
    path("list/", views.BlogList.as_view(), name='blog-list'),
    path("comment/delete/<int:id>/", views.CommentDelete.as_view(), name='delete-comment'),
]