from rest_framework import serializers

from apps.comment.serializers import CommentListSerializer
from apps.post.models import Post


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        exclude = ('like',)


class PostCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['title', 'text', 'user']


class PostDetailSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    comments = CommentListSerializer(source='posts_comment', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'text', 'published', 'like_count', 'views_count', 'comments']


class PostUpdateSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': False},
            'text': {'required': False},
        }


class PostDeleteSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = '__all__'
