from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase

from blog.models import *


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = Category.objects.create(
            title='test_group',
            slug='test_slug_group'
        )

    def setUp(self) -> None:
        self.guest_client = Client()
        self.user = get_user_model().objects.create_user(username='test_user')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        small_gif = (b'\x47\x49\x46\x38\x39\x61\x02\x00'
                     b'\x01\x00\x80\x00\x00\x00\x00\x00'
                     b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
                     b'\x00\x00\x00\x2C\x00\x00\x00\x00'
                     b'\x02\x00\x01\x00\x00\x02\x02\x0C'
                     b'\x0A\x00\x3B'
                     )

        self.uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )

        self.post = Post.objects.create(
            title='test_title',
            slug='test_post_slug',
            author=self.user,
            image=self.uploaded,
            pub_date='12.04.2021',
            category=self.category
        )

        self.post = Post.objects.get()

        self.comment = Comment.objects.create(
            post=self.post,
            comment_author=self.user,
            text='testtext',
            created='12.04.2021'
        )

        self.comment = Comment.objects.get()
