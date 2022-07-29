from ..models import Tag, Post, Category
from ..serializers import TagSerializer, PostSerializer, PostCreateSerializer
from rest_framework.response import Response
from rest_framework import generics, status, permissions, authentication


class TagListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/blog/api/tag/list/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/blog/api/tag/create/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/blog/api/tag/rud/<int:pk>/
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/blog/api/post/list/
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/blog/api/post/create/
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PostRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/blog/api/post/rud/<int:pk>/
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
