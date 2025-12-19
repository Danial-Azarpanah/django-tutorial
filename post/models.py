from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "مقاله"  # تغییر نحوه نمایش اسم مفرد مدل در پنل ادمین
        verbose_name_plural = "مقالات"  # تغییر نحوه نمایش اسم جمع مدل در پنل ادمین