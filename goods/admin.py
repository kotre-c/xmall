from django.contrib import admin

# Register your models here.
from goods.models import Good, GoodImage, Category

# admin.site.register(Good)
# admin.site.register(GoodImage)
admin.site.register(Category)


class GoodImageInline(admin.TabularInline):
    model = GoodImage


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['productName', 'salePrice', 'created', 'updated']
    inlines = [GoodImageInline]
