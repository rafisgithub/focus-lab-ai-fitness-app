from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from apps.products.models import Product, Size, Color, ProductVariant, Category, Subcategory


class ProductVariantInline(TabularInline):
    model = ProductVariant
    extra = 0
    # autocomplete_fields = ['size', 'color']
    autocomplete_fields = ['size', 'color']

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



@admin.register(Subcategory)
class SubcategoryAdmin(ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    autocomplete_fields = ('category',)

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [ProductVariantInline]


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Color)
class ColorAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ProductVariant)
class ProductVariantAdmin(ModelAdmin):
    list_display = ('product', 'size', 'color', 'price', 'stock')
