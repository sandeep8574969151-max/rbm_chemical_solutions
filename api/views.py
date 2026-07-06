from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Q

from .models import Banner, GeneralProduct, Enquiry, Category, Product, Gallery
from .serializers import BannerSerializer, ProductSerializer, GeneralProductSerializer, GallerySerializer

@api_view(['GET'])
def get_banners(request):
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_categories(request):
    data = {}
    categories = Category.objects.all()
    for cat in categories:
        subs = Product.objects.filter(category=cat).exclude(sub_category__isnull=True).exclude(sub_category='').values_list('sub_category', flat=True).distinct()
        data[cat.name] = list(subs)
    return JsonResponse(data)

@api_view(['GET'])
def get_products(request):
    products = GeneralProduct.objects.all() 
    serializer = GeneralProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_detail(request, id):
    product = get_object_or_404(GeneralProduct, id=id)
    serializer = GeneralProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def get_products_by_category(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_products_by_subcategory(request, sub_category_name):
    products = Product.objects.filter(sub_category=sub_category_name)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_gallery(request):
    try:
        images = Gallery.objects.all().order_by('-created_at')
        serializer = GallerySerializer(images, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def get_general_product_detail(request, id):
    product = get_object_or_404(GeneralProduct, id=id)
    serializer = GeneralProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def save_enquiry(request):
    return Response({"message": "Enquiry saved successfully!"})

@api_view(['POST'])
def upload_product(request):
    return Response({"message": "Product Uploaded!"})