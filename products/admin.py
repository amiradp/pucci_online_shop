from django.contrib import admin

from .models import Category, Product, Vendor, Images, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

   list_display = ['name', 'slug']
   prepopulated_fields = {'slug': ('name',)}
   

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

   list_display = ['name', 'slug']
   prepopulated_fields = {'slug': ('name',)}


class ProductImagesInline(admin.StackedInline):
    model = Images


class CommentInLine(admin.TabularInline):
   model = Comment
   fields = ['author', 'body', 'active', ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ['name', 'slug', 'price', 'quantity', 'size', 'available', 'created', 'updated']
   list_filter = ['available', 'created', 'updated']
   list_editable = ['price', 'available']
   prepopulated_fields = {'slug': ('name',)}

   inlines = [
      ProductImagesInline,
      CommentInLine
      ]
   
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'active', ]