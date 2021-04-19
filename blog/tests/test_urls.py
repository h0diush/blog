from django.test import Client
from django.urls import reverse

from .base import BaseTestCase


class PostUrlsTest(BaseTestCase):

    def test_index_guest_client(self):
        """ Тест главной страницы неавторизованным пользователем """
        response = self.guest_client.get(reverse('index'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к главной странице')

    def test_index_authorized_client(self):
        """ Тест главной страницы авторизованным пользователем """
        response = self.authorized_client.get(reverse('index'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к главной странице')

    def test_posts_guest_client(self):
        """ Тест страницы с постами """
        response = self.guest_client.get(reverse('posts'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице с постами')

    def test_post_guest_client(self):
        """ Тест страницы с постом неавторизованным пользователем """
        response = self.guest_client.get(
            reverse('post', kwargs={'post_slug': 'test_post_slug'}))
        self.assertEquals(
            response.status_code,
            302,
            'Только авторизованный пользователь может подключиться к странице')

    def test_post_authorized_client(self):
        """ Тест страницы с постом авторизованным пользователем """
        response = self.authorized_client.get(
            reverse('post', kwargs={'post_slug': 'test_post_slug'}))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице с постом')

    def test_group_authorized_client(self):
        """ Тест страницы с группами авторизованным пользователем """
        response = self.authorized_client.get(
            reverse('group', kwargs={'group_slug': 'test_slug_group'}))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице с группами')

    def test_group_guest_client(self):
        """ Тест страницы с группами неавторизованным пользователем """
        response = self.guest_client.get(
            reverse(
                'group', kwargs={
                    'group_slug': 'test_slug_group'}))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице с группами')

    def test_add_post_authorized_client(self):
        """ Тест страницы добавления поста авторизованным пользователем """
        response = self.authorized_client.get(reverse('add_post'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице с добавлением поста')

    def test_add_post_guest_client(self):
        """ Тест страницы добавления поста авторизованным пользователем """
        response = self.guest_client.get(reverse('add_post'))
        self.assertEquals(
            response.status_code,
            403,
            'Только авторизованный пользователь может подключиться к странице')

    def test_contact(self):
        """ Тест страницы с контактами """
        response = self.guest_client.get(reverse('contact'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице')

    def test_about(self):
        """ Тест страницы с обратной связью """
        response = self.guest_client.get(reverse('about'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице')

    def test_register(self):
        """ Тест страницы с регистрацией"""
        response = self.guest_client.get(reverse('register'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице')

    def test_login(self):
        """ Тест страницы авторизации """
        response = self.guest_client.get(reverse('login'))
        self.assertEquals(
            response.status_code,
            200,
            'Невозможно подключиться к странице')
