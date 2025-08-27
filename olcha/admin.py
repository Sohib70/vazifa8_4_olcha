from django.contrib import admin
from .models import Category
# Register your models here.

@admin.register(Category)
class CateforyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
