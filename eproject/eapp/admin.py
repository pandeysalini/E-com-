from django.contrib import admin
from .models import Category,Product,cart
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display=['name','description']
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
  list_display=['p_name','p_price','p_description','user']
admin.site.register(Product,ProductAdmin)
