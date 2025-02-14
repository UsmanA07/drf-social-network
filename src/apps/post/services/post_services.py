from apps.post.dto.post_dto import PostListDTO

from apps.post.repository.post_repositories import PostRepository


class PostServices:
    def __init__(self):
        self.repository = PostRepository()
        print(f'init: {self.repository}')

    def post_list(self):
        print(f'post_list: {self.repository}')
        print(f'post_list: {self.repository.all_post()}')
        return self.repository.all_post()



























# def post_create(request):
#     print(request)
#     post = PostCreateSerializer(data=request.data)
#     print(post, 'post')
#     if post.is_valid():
#         return post.save(user=request.user)
#
#
# def post_detail(pk: int):
#     return Post.objects.get(pk=pk)
#
#
# def post_delete(pk: int):
#     post = Post.objects.get(pk=pk)
#     post.delete()
#
#
# def post_update(pk: int, request):
#     post = Post.objects.get(pk=pk)
#     serializer = PostUpdateSerializers(post, data=request.data)
#     if serializer.is_valid():
#         serializer.validated_data['published'] = datetime.now()
#         serializer.save()
