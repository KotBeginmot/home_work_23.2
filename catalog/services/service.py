from django.core.cache import cache

from config.settings import CACHE_ENABLE


def cash_catalog(queryset):

    if CACHE_ENABLE:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = queryset
            cache.set(key, category_list)
        return category_list
    else:
        return queryset
