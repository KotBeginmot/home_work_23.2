from django.urls import path
from django.views.decorators.cache import never_cache

from blogrecord.apps import BlogrecordConfig
from blogrecord.views import BlogListView, BlogCreateView, BlogDetailView, BlogDeleteView, BlogUpdateView

app_name = BlogrecordConfig.name

urlpatterns = [
    path('list/', never_cache(BlogListView.as_view()), name='list'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('detail/<int:pk>', never_cache(BlogDetailView.as_view()), name='detail'),
    path('delete/<int:pk>', never_cache(BlogDeleteView.as_view()), name='delete'),
    path('update/<int:pk>', never_cache(BlogUpdateView.as_view()), name='update'),

]
