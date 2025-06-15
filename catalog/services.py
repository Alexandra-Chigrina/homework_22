from catalog.models import Product
from django.core.cache import cache
from django.db.models import Q

from config.settings import CACHE_ENABLED


def get_products_by_category(category_id, user=None):
    """Возвращает список всех продуктов в указанной категории"""
    if not CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    key = f"products_by_category_{category_id}"
    products = cache.get(key)
    if products is None:
        query = Product.objects.filter(category_id=category_id)
        if user and user.is_authenticated:
            query = query.filter(Q(status="published") | Q(owner=user))
        else:
            query = query.filter(status="published")
        products = list(query.order_by("-created_at"))
        cache.set(key, products, 60 * 15)

    return products
