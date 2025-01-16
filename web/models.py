from django.db import models

# Create your models here.
class Connect(models.Model):
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name  # 在 admin 中顯示名稱
