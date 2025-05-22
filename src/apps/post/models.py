from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=256,
        blank=False,
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
    like_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        indexes = [
            models.Index(fields=['-published'])
        ]
