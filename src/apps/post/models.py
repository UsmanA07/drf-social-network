from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        blank=True,
        verbose_name='Текст'
    )
    published = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата публикации'
    )
    like = models.ManyToManyField(
        User,
        related_name='liked_posts',
        blank=True,
        verbose_name='Лайки'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        indexes = [
            models.Index(fields=['-published'])
        ]


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )
    like = models.ManyToManyField(
        User,
        related_name='liked_comments',
        blank=True,
        verbose_name='Лайки'
    )
    published = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата публикации'
    )

    def __str__(self):
        return f"Комментарий от {self.user} к посту '{self.post}'"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        indexes = [
            models.Index(fields=['-published'])
        ]
