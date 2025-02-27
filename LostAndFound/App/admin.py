from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Item
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status', 'reported_by', 'date_reported')
    list_filter = ('status', 'category')
    search_fields = ('title', 'location', 'description')
    readonly_fields = ('date_reported',)


admin.site.unregister(User)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')

