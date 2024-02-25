from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image']

class AdditionalInfoTabular(admin.TabularInline): 
    model=Additional_Information

class AdditionalImageTabular(admin.TabularInline):
    model=Additional_Images  

class shortDescriptionTabular(admin.TabularInline):
    model=Short_Description

class ProductAdmin(admin.ModelAdmin):
    inlines=[shortDescriptionTabular,AdditionalInfoTabular,AdditionalImageTabular]
    list_display=['title','product_image','price']

admin.site.register(Product,ProductAdmin)

admin.site.register(Category,CategoryAdmin)