from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from user.models import NewUser
from user.serializers import RegisterUserSerializers
from blog.models import Post
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission, AllowAny, IsAdminUser, \
    IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, DjangoModelPermissions
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from .serializers import PostSerializer, PostSerializerCreate, PostSerializerUpdate
from rest_framework import viewsets
from rest_framework import filters



class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     # authentication_classes = [JWTTokenUserAuthentication]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


    # Define Custom Queryset

    # def get_object(self, queryset=None, **kwargs):
    #     print('here')
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=item)

    # def get_object(self):
    #     print('ger')
    #     slug = self.request.query_params.get('slug', None)
    #     print(Post.objects.filter(slug='title'))
    #     return Post.objects.filter(slug=slug)

    #
    # def get_queryset(self):
    #
    #     user = self.request.user
    #
    #     return Post.objects.filter(author=user)

    def filter_queryset(self, request):
        user = self.request.user

        return Post.objects.filter(author=user)


class PostListDetailFilter(generics.ListAPIView):

    queryset = Post.objects.all()

    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


# '^' start-with
# '=' Ecact matches
# '@' Full-text search
# '$' Regex search


# class CreatePost(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class AdminPostUpload(APIView):
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminPostDetail(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class EditPost(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializerUpdate




# class EditPost(APIView):
#     def put(self, request, pk, format=None):
#         post = Post.objects.get(id=pk)
#         post.title = request.form.gr
#

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer









    """ Concrete View Classes
    # CreateAPIView
    Used for create-only endpoints.
    # ListAPIView
    Used for read-only endpoints to represent a collection of model instances.
    # RetrieveAPIView
    Used for read-only endpoints to represent a single model instance.
    # DestroyAPIView
    Used for delete-only endpoints for a single model instance.
    # UpdateAPIView
    Used for update-only endpoints for a single model instance.
    # ListCreateAPIView
    Used for read-write endpoints to represent a collection of model instances.
    RetrieveUpdateAPIView
    Used for read or update endpoints to represent a single model instance.
    # RetrieveDestroyAPIView
    Used for read or delete endpoints to represent a single model instance.
    # RetrieveUpdateDestroyAPIView
    Used for read-write-delete endpoints to represent a single model instance.
    """


# class GETT(APIView):
#     def get(self, request):
#         post = Post.objects.filter(id=2).first()
#         print(post)
#         return HttpResponse(post.category.name)
