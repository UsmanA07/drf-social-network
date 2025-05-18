from rest_framework import serializers

from apps.comment.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['post', 'text', 'user']


class CommentUpdateSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    # post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['text']
