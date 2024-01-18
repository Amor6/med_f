from django.contrib import admin

from main.models import Category, Services


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name_serv', 'category', 'pk',)
