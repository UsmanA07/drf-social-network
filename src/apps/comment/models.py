from django.contrib.auth import get_user_model
from django.db import models

from apps.comment.services.model_services import str_mapping
from apps.post.models import Post

User = get_user_model()


class Comment(models.Model):
    objects = None
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='posts_comment',
        verbose_name='Пост'
    )
    text = models.TextField(
        blank=True,
        verbose_name='Текст'
    )
    published = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return str_mapping(str(self.text))

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        indexes = [
            models.Index(fields=['-published'])
        ]
