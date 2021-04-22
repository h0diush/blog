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

    def like(self, **kwargs):
        context = kwargs
        post = Post.objects.get(slug=self.kwargs['post_slug'])
        likes = post.likes.all()
        post_likes = []
        like_bool = False
        for us in likes:
            user_like = us.user
            post_likes.append(user_like)
        if self.request.user in post_likes:
            like_bool = True
        count = post.likes.count()
        context['like_bool'] = like_bool
        context['count_like'] = count
        context['likes'] = likes
        return context

    def subscription(self, **kwargs):
        context = kwargs
        user = UserProfile.objects.get(username=self.kwargs['username'])
        followers =[]
        follow = False
        following = user.following.all()
        for us in following:
            author_fol = us.user
            followers.append(author_fol)
        if self.request.user in followers:
            follow = True
        context['subscribers'] = user.following.count()
        context['subscription'] = user.follower.count()
        context['follow_bool'] = follow
        return context
