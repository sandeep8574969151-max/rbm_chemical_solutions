from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, Gallery

@receiver(post_save, sender=Product)
def add_product_to_gallery(sender, instance, created, **kwargs):
    # Agar naya product create hua hai aur usme image hai
    if created and instance.image:
        Gallery.objects.create(image=instance.image)