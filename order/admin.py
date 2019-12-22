from django.contrib import admin

# Register your models here.
from order.models import OrderGoods, Order


class OrderGoodInline(admin.TabularInline):
    model = OrderGoods


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_sn', 'pay_status', 'created', 'updated']
    inlines = [OrderGoodInline]