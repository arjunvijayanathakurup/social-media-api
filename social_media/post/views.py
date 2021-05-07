from django.shortcuts import render
from rest_framework import generics, permissions
from post.models import Post, Like, DisLike
from post.serializers import PostSerializer,\
        LikeSerializers,\
        DisLikeSerializers, \
        LikePostSerializers, \
        DislikePostSerializers


class PostList(generics.ListCreateAPIView):
    """
        PostList provides the List & Create API 
        endpoint for new posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    ordering = ['-weight']
    def perform_create(self, serializer):           
        serializer.save(owner=self.request.user)


class LikeList(generics.ListAPIView):
    """
        LikeList provides the List API view 
        endpoint for accessing the liked posts
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializers


class DisLikeList(generics.ListAPIView):
    """
        DisLikeList provides the List API view endpoint 
        for accessing the disliked posts
    """
    queryset = DisLike.objects.all()
    serializer_class = DisLikeSerializers


class LikePost(generics.ListCreateAPIView):
    """
        LikePost provides the List & Create API view 
        endpoint for performing like operations on posts
    """
    queryset = Like.objects.all()
    serializer_class = LikePostSerializers
    permission_classes = (permissions.IsAuthenticated,)


class DisLikePost(generics.ListCreateAPIView):
    """
        DisLikePost provides the List & Create API view 
        endpoint for performing dislike operations on posts
    """
    queryset = DisLike.objects.all()
    serializer_class = DislikePostSerializers
    permission_classes = (permissions.IsAuthenticated,)