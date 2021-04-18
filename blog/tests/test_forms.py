from django.urls import reverse
from blog.models import *
from .base import BaseTestCase
from django.core.files.uploadedfile import SimpleUploadedFile


class TestForms(BaseTestCase):
    def test_create_post(self):
        """Валидная форма создает post."""
        category = Category.objects.create(
            title = 'test_title',
            slug = 'test_slug'
        )

        small_gif = (b'\x47\x49\x46\x38\x39\x61\x02\x00'
                     b'\x01\x00\x80\x00\x00\x00\x00\x00'
                     b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
                     b'\x00\x00\x00\x2C\x00\x00\x00\x00'
                     b'\x02\x00\x01\x00\x00\x02\x02\x0C'
                     b'\x0A\x00\x3B'
                     )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )

        post_count = Post.objects.count()

        form_data = {
            'title': self.post.title,
            'category': category.id,
            'image': uploaded,
            'slug': self.post.slug,
            'content': 'test test test'
        }

        response = self.authorized_client.post(
            reverse('add_post'),
            data=form_data,
            follow=True
        )

        post = response.context['posts'][0]

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Post.objects.count(), post_count + 1)
        self.assertEqual(post.text, form_data['text'])
        self.assertEqual(post.group.id, form_data['group'])