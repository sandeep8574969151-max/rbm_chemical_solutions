from django.contrib import admin
from .models import Banner, GeneralProduct, Enquiry, Category, Product
from .models import ClientSlider



admin.site.register(ClientSlider)

# Banner ko simple register kiya
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)

# GeneralProduct ko register kiya
@admin.register(GeneralProduct)
class GeneralProductAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Enquiry ko register kiya
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

# Category ko register kiya
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

# Product ko register kiya (Ab import hone ke karan error nahi aayega)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sub_category')
    list_filter = ('category',)