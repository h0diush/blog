from django import forms
from django.urls import reverse

from blog.models import *

from .base import BaseTestCase


class PostPagesTest(BaseTestCase):
    def test_posts_uses_correct_template(self):
        """Соответствие URL-адресов HTML-шаблонам"""
        templates_pages_names = {
            'posts/index.html': reverse('index'),
            'posts/groups.html': reverse('group', kwargs={'group_slug': 'test_slug_group'}),
            'posts/add_post.html': reverse('add_post'),
            'posts/posts.html': reverse('posts'),
            'posts/about.html': reverse('about'),
            'posts/contact.html': reverse('contact'),
            'users/login.html': reverse('login'),
            'users/register.html': reverse('register'),
        }

        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_homepage_shows_correct_context(self):
        """context главной страницы"""
        response = self.guest_client.get(reverse('index'))
        post_title = response.context.get('three_post')[0].title
        post_author = response.context.get('three_post')[0].author
        post_category = response.context.get('three_post')[0].category
        post_image = response.context.get('three_post')[0].image
        self.assertEqual(post_title, 'test_title')
        self.assertEqual(post_author, self.user)
        self.assertEqual(post_category, PostPagesTest.category)
        self.assertEqual(post_image.size, self.uploaded.size)

    def test_group_page_show_correct_context(self):
        """context страницы с группами"""
        response = self.authorized_client.get(reverse("group",
                                                      kwargs={"group_slug": "test_slug_group"}))
        post_title = response.context.get("three_post")[0].title
        post_author = response.context.get("three_post")[0].author
        post_pub_date = response.context.get("three_post")[0].pub_date
        post_category = response.context.get("three_post")[0].category
        post_image = response.context.get("three_post")[0].image
        self.assertEqual(post_title, self.post.title)
        self.assertEqual(post_author, self.user)
        self.assertEqual(post_pub_date, self.post.pub_date)
        self.assertEqual(post_category, self.category)
        self.assertEqual(post_image.size, self.uploaded.size)
