from django.contrib import admin
from .models import Category, Product, Brand, Store, Employee, Supplier, Review, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug']
    list_filter = ['parent']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'stock', 'is_available', 'created_at']
    list_filter = ['is_available', 'category', 'brand']
    list_editable = ['price', 'stock', 'is_available']
    search_fields = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description_short']
    search_fields = ['name', 'description']

    def description_short(self, obj):
        if obj.description and len(obj.description) > 80:
            return obj.description[:80] + '...'
        return obj.description or '—'
    description_short.short_description = 'Описание'


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'working_hours']
    search_fields = ['name', 'address']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'store', 'has_photo']
    list_filter = ['store', 'position']
    search_fields = ['first_name', 'last_name', 'position']
    fields = ['first_name', 'last_name', 'position', 'store', 'photo']

    def has_photo(self, obj):
        return '✅' if obj.photo else '❌'
    has_photo.short_description = 'Фото'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_email', 'contact_phone', 'has_logo']
    search_fields = ['name', 'contact_email']
    fields = ['name', 'contact_email', 'contact_phone', 'logo']

    def has_logo(self, obj):
        return '✅' if obj.logo else '❌'
    has_logo.short_description = 'Логотип'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'rating', 'text_short', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['author', 'text', 'product__name']

    def text_short(self, obj):
        if len(obj.text) > 60:
            return obj.text[:60] + '...'
        return obj.text
    text_short.short_description = 'Текст отзыва'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'customer_name', 'customer_phone', 'store', 'quantity', 'status', 'created_at']
    list_filter = ['status', 'store', 'created_at']
    list_editable = ['status']
    search_fields = ['customer_name', 'customer_phone', 'product__name']