from django.contrib import admin

# Register your models here.
from home.models import NavList, Panelcontent, Panel

admin.site.register(NavList)


class PanelcontentInline(admin.TabularInline):
    model = Panelcontent


@admin.register(Panel)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
    inlines = [PanelcontentInline]
