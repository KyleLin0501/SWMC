from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Connect

@admin.register(Connect)
class ConnectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'phone')  # 顯示在列表的欄位
    search_fields = ('name', 'company_name', 'email')          # 搜索功能欄位
    list_filter = ('company_name',)                            # 篩選條件