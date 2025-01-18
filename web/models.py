from django.db import models
from django.utils.timezone import now
from django.core.files.base import ContentFile
from django.utils.html import format_html
# Create your models here.



class Case(models.Model):
    company_name = models.CharField(max_length=50)
    company_img = models.ImageField(upload_to='image/case/')

    def __str__(self):
        return self.company_name

    # 用於顯示圖片的函數
    def company_img_preview(self):
        if self.company_img:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />', self.company_img.url)
        return "無圖片"

    company_img_preview.short_description = "圖片預覽"


class Connect(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name  # 在 admin 中顯示名稱

