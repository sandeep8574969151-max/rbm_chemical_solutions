from django.urls import path
from . import views  # Ensure 'views' is imported

urlpatterns = [
    path('get_banners/', views.get_banners, name='get_banners'),
    path('get_categories/', views.get_categories, name='get_categories'),
    path('get_products/', views.get_products, name='get_products'),
    path('get_product_detail/<int:id>/', views.get_product_detail, name='get_product_detail'),
    path('save_enquiry/', views.save_enquiry, name='save_enquiry'),
    path('get_products_by_category/<str:category_name>/', views.get_products_by_category, name='get_products_by_category'),
    path('get_products_by_subcategory/<str:sub_category_name>/', views.get_products_by_subcategory, name='get_products_by_subcategory'),
    path('get_gallery/', views.get_gallery, name='get_gallery'),
    
]