from rest_framework import serializers
from django.contrib.auth.models import User
from post.models import Post, Like, DisLike


class PostSerializer(serializers.ModelSerializer):
    """
        Post Serializer
    """
    class Meta:
        model = Post
        fields = ('id', 'name', 'description', 'image', 'tags', 'status', 'created_at')


class LikeSerializers(serializers.ModelSerializer):
    """
        Like Serializer
    """
    post = PostSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Like
        fields = ('user', 'post')


class DisLikeSerializers(serializers.ModelSerializer):
    """
        Dislike Serializer
    """

    post = PostSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = DisLike
        fields = ('user', 'post')


class LikePostSerializers(serializers.ModelSerializer):
    """
        Like Post Serializer
    """
    class Meta:
        model = Like
        fields = ('user', 'post')


class DislikePostSerializers(serializers.ModelSerializer):
    """
        Dislike Post Serializer
    """
    class Meta:
        model = DisLike
        fields = ('user', 'post')