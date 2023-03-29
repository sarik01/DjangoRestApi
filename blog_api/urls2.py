from django.urls import path
from .views import PostListDetailFilter

app_name = 'blog_api2'

urlpatterns = [
    path('custom/', PostListDetailFilter.as_view(), name='filter_search'),


]