from api.v1.post.serializers import PostCreateSerializer, PostUpdateSerializers
from apps.post.models import Post
from datetime import datetime


def post_list():
    return Post.objects.all()


def post_create(request, **kwargs):
    print(request)
    task = PostCreateSerializer(data=request.data)
    print(task, 'task')
    if task.is_valid():
        return task.save(user=request.user)


def post_detail(pk: int, **kwargs):
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
