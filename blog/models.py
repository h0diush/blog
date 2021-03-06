import random
import string

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits)
                   for _ in range(6))


class Role(models.TextChoices):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


class UserProfile(AbstractUser):
    avatar = models.ImageField(
        upload_to='users_avatar/',
        null=True,
        verbose_name='Аватар',
        blank=True)

    role = models.CharField(
        max_length=10,
        verbose_name='Роль',
        choices=Role.choices,
        default=Role.USER
    )

    @property
    def user_role(self):
        return self.role

    def get_absolute_url(self):
        return reverse('user', kwargs={'username': self.username})

    class Meta(AbstractUser.Meta):
        pass


class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL', unique=True)

    def get_absolute_url(self):
        return reverse('group', kwargs={'group_slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL', unique=True)
    content = models.TextField(verbose_name='Контент')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации')
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='posts')
    image = models.ImageField(
        upload_to='posts/',
        verbose_name='Картинка',
        null=True,
        blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
        related_name='posts')
    tags = TaggableManager(blank=True, verbose_name='Тэги')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify((rand_slug() + '-' + self.title))
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='comments')
    comment_author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
        related_name='comments')
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время комментария')
    text = models.TextField(verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return f'{self.comment_author} -> {self.text}'


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    email = models.EmailField(verbose_name='Электронная почта')
    subject = models.CharField(max_length=50, verbose_name='Предмет')
    text = models.TextField(verbose_name='Текст сообщения')

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.email} -> {self.text}'


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Пост',
        related_name='likes')
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='likes')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = "Лайки"

    def __str__(self) -> str:
        return f'{self.user} -> {self.post}'


class Follow(models.Model):
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Подписка',
        related_name='following')
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'], name='unique_follow')]

    def __str__(self) -> str:
        return '%s подписался на %s' % (self.author, self.user)
