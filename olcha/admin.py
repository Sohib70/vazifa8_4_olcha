from django.contrib import admin
from .models import Category,Product,Image
# Register your models here.

@admin.register(Category)
class CateforyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Product)
admin.site.register(Image)