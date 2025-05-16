from django.contrib.auth import get_user_model
from django.db import models

from apps.post.models import Post

User = get_user_model()


class Comment(models.Model):
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
        return f'{str(self.text).split()[0:3]}...'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        indexes = [
            models.Index(fields=['-published'])
        ]
