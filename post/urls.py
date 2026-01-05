from django.urls import path

from . import views


urlpatterns = [
    path("detail/<str:slug>/", views.BlogDetail.as_view(), name='blog-detail'),
]