from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import *
from django.utils.html import format_html
from image_cropping import ImageCroppingMixin

@admin.register(Connect)
class ConnectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'phone')  # 顯示在列表的欄位
    search_fields = ('name', 'company_name', 'email')          # 搜索功能欄位
    list_filter = ('company_name',)        # 篩選條件


@admin.register(Case)
class CompanyCase(admin.ModelAdmin):
    list_display = ('company_name', 'company_img_preview')  # 顯示圖片預覽
    search_fields = ('company_name',)
    list_filter = ('company_name',)
    readonly_fields = ('company_img_preview',)  # 使圖片預覽欄位不可編輯

    # 預覽圖片
    def company_img_preview(self, obj):
        if obj.company_img:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.company_img.url)
        return "無圖片"

    company_img_preview.short_description = "圖片預覽"
