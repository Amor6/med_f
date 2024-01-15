from django.contrib import admin

from main.models import Category
# ,Services, Offer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)

#