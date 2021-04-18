from blog.models import *
from django.urls import reverse
from django import forms
from .base import BaseTestCase


class PostPagesTest(BaseTestCase):

    # Проверяем используемые шаблоны
    def test_posts_uses_correct_template(self):
        """Соответствие URL-адресов HTML-шаблонам"""
        templates_pages_names = {
            'posts/index.html': reverse('index'),
            'posts/groups.html': reverse('group', kwargs={'group_slug': 'test_slug_group'}),
            'posts/add_post.html': reverse('add_post'),
            'posts/posts.html': reverse('posts'),
            'posts/post.html': reverse('post', kwargs={'post_slug': 'test_post_slug'})
        }

        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    # # проверяем context
    # def test_homepage_shows_correct_context(self):
    #     """context главной страницы"""
    #     response = self.authorized_client.get(reverse('index'))
    #     post_text = response.context.get('page')[0].text
    #     post_author = response.context.get('page')[0].author
    #     post_group = response.context.get('page')[0].group
    #     post_image = response.context.get('page')[0].image
    #     self.assertEqual(post_text, 'testtext')
    #     self.assertEqual(post_author, self.user)
    #     self.assertEqual(post_group, PostPagesTest.group)
    #     self.assertEqual(post_image.size, self.uploaded.size)

    # def test_group_page_show_correct_context(self):
    #     """context страницы с группами"""
    #     response = self.authorized_client.get(reverse("slug",
    #                                                   kwargs={"slug": "testslug"}))
    #     post_text = response.context.get("page")[0].text
    #     post_author = response.context.get("page")[0].author
    #     post_pub_date = response.context.get("page")[0].pub_date
    #     post_group = response.context.get("page")[0].group
    #     post_image = response.context.get("page")[0].image
    #     self.assertEqual(post_text, self.post.text)
    #     self.assertEqual(post_author, self.user)
    #     self.assertEqual(post_pub_date, self.post.pub_date)
    #     self.assertEqual(post_group, self.group)
    #     self.assertEqual(post_image.size, self.uploaded.size)

    # def test_profile_page_show_correct_context(self):
    #     """context страницы пользователя"""
    #     response = self.authorized_client.get(
    #         reverse("profile", kwargs={'username': 'testuser'}))
    #     post_text = response.context.get("page")[0].text
    #     post_author = response.context.get("page")[0].author
    #     post_pub_date = response.context.get("page")[0].pub_date
    #     post_group = response.context.get("page")[0].group
    #     post_image = response.context.get("page")[0].image
    #     self.assertEqual(post_text, self.post.text)
    #     self.assertEqual(post_author, self.user)
    #     self.assertEqual(post_pub_date, self.post.pub_date)
    #     self.assertEqual(post_group, self.group)
    #     self.assertEqual(post_image.size, self.uploaded.size)