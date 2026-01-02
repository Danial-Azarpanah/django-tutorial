from django.db import models


class Info(models.Model):
    contact_number = models.CharField(max_length=11, verbose_name="شماره تماس")
    email = models.EmailField(verbose_name="ایمیل")
    address = models.TextField(verbose_name="آدرس")

    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات"

    def __str__(self):
        return f"{self.contact_number} - {self.email}"


class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="آدرس ایمیل")
    subject = models.CharField(max_length=50, verbose_name="موضوع")
    body = models.TextField(verbose_name="متن")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"
        ordering = ("-created_at",)
    
    def __str__(self):
        return f"{self.subject}: {self.body[:50]}"