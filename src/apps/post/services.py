from api.v1.post.serializers import PostCreateSerializer, PostUpdateSerializers
from apps.post.models import Post
from datetime import datetime


def post_list():
    return Post.objects.all()


def post_create(request):
    print(request)
    post = PostCreateSerializer(data=request.data)
    print(post, 'post')
    if post.is_valid():
        return post.save(user=request.user)


def post_detail(pk: int):
    return Post.objects.get(pk=pk)


def post_delete(pk: int):
    post = Post.objects.get(pk=pk)
    post.delete()


def post_update(pk: int, request):
    post = Post.objects.get(pk=pk)
    serializer = PostUpdateSerializers(post, data=request.data)
    if serializer.is_valid():
        serializer.validated_data['published'] = datetime.now()
        serializer.save()
