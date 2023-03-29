from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostList, PostListDetailFilter, AdminPostUpload, AdminPostDetail, EditPost, DeletePost

app_name = 'blog_api'

router = DefaultRouter()
router.register('', PostList, basename='user')
# router.register('search2/', PostListDetailFilter, basename='postsearch')
urlpatterns =[
    path('', include(router.urls)),
    path('admin/create/', AdminPostUpload.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='adminpostdetail'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),


]