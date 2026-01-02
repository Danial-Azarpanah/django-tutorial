from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(null=True, unique=True, verbose_name="اسلاگ", allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجادس")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی‌ها"
    
    def __str__(self):
        return self.title



class Article(models.Model): 
    title = models.CharField(max_length=50, verbose_name="عنوان")
    slug = models.SlugField(unique=True, verbose_name="اسلاگ", allow_unicode=True, null=True)
    image = models.ImageField(null=True, upload_to="article_images", verbose_name="تصویر")
    body = models.TextField(verbose_name="بدنه")
    is_published = models.BooleanField(default=True, verbose_name="منتشر شده")
    view_count = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدید")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    category = models.ForeignKey(Category, related_name="articles", on_delete=models.SET_NULL, null=True, verbose_name="دسته بندی")
    author = models.ForeignKey(
        User,
        related_name="articles", on_delete=models.CASCADE,
        verbose_name="نویسنده", null=True
    )

    class Meta:
        verbose_name = "مقاله"  # تغییر نحوه نمایش اسم مفرد مدل در پنل ادمین
        verbose_name_plural = "مقالات"  # تغییر نحوه نمایش اسم جمع مدل در پنل ادمین

    def __str__(self):
        return self.title