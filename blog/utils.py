from .models import *


class DataMixin:
    model = Post

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['cats'] = cats
        context['banner'] = Post.objects.all()[:5]
        context['three_post'] = Post.objects.all()[:3]
        return context

    def cont_comment(self, slug, **kwargs):
        context = kwargs
        count = Comment.objects.filter(post__slug=slug).count()
        res = count % 10
        if count == 0:
            comment_count = 'Нет комментариев'
        elif res == 1:
            comment_count = f'{count} Комментарий'
        elif count > 4 and count < 21:
            comment_count = f'{count} Комментариев'
        elif res > 1 and res < 5:
            comment_count = f'{count} Комментария'
        else:
            comment_count = f'{count} Комментариев'
        context['count'] = comment_count
        return context
