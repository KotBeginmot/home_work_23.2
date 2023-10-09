from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import home, ContactsCreateView, ProductsListView, CategoryProductsListView, ProductCreateView, \
    ProductUpdateView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView, ProductDeleteView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('category_product/<int:pk>/', never_cache(CategoryProductsListView.as_view()), name='category_product'),
    path('', home, name='home'),
    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete')

]
