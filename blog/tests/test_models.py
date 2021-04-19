from django.test import TestCase

from .base import BaseTestCase


class PostModelsTest(BaseTestCase):
    def test_verbose_name(self):
        post = self.post
        field_verboses = {
            'title': 'Заголовок',
            'slug': 'URL',
            'content': 'Контент',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'category': 'Категория',
            'image': 'Картинка',
            'tags': 'Тэги',
        }

        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    post._meta.get_field(value).verbose_name, expected)


class CategoryModelsTest(BaseTestCase):
    def test_verbose_name(self):
        category = self.category
        field_verboses = {
            'title': 'Заголовок',
            'slug': 'URL',
        }

        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    category._meta.get_field(value).verbose_name, expected)


class CommentModelsTest(BaseTestCase):
    def test_verbose_name(self):
        comment = self.comment
        field_verboses = {
            'post': 'Пост',
            'created': 'Дата и время комментария',
            'comment_author': 'Автор комментария',
            'text': 'Текст комментария'
        }

        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    comment._meta.get_field(value).verbose_name, expected)
