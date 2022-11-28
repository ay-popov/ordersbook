from typing import TYPE_CHECKING
from django.contrib import admin

from .models import Order, Equipment, Devision

if TYPE_CHECKING:
    admin.site: admin.AdminSite


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Сотрудники"

    list_display = "pk", "name", "order_date"
    list_display_links = "name",
    ordering = "name", "pk"


@admin.register(Equipment)
class Equipment(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Оборудование"

    list_display = "pk", "name",
    list_display_links = "name",
    ordering = "name", "pk"

    def __str__(self):
        return self.name


@admin.register(Devision)
class Devision(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Участки"

    list_display = "pk", "name",
    list_display_links = "name",
    ordering = "name", "pk"

    def __str__(self):
        return self.name
