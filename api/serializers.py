from rest_framework import serializers
from .models import Banner, GeneralProduct, Product, Gallery

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

# Yeh General Products ke liye hai (Home page/Our Products)
class GeneralProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralProduct
        fields = '__all__'

# Yeh Category/Sub-category wale products ke liye hai
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'features', 'applications', 'benefits', 'image', 'category', 'sub_category']
        
        
        
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image']        