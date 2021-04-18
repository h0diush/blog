from django.contrib.auth import login, logout, mixins, views
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, edit, UpdateView,
                                  DeleteView)
# from django.core.mail import send_mail  -> send email on the mail

from .forms import *
from .models import *
from .utils import DataMixin


class HomePage(DataMixin, ListView):
    context_object_name = 'posts'
    template_name = 'posts/index.html'

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')
        if search_query:
            posts = Post.objects.filter(title__icontains=search_query)
        else:
            posts = Post.objects.all()[:3]
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(mixin.items()))


class PostsView(DataMixin, ListView):
    context_object_name = 'posts'
    template_name = 'posts/posts.html'
    raise_exception = True
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Последние посты')
        return dict(list(context.items()) + list(mixin.items()))


class ShowGroup(DataMixin, ListView):
    template_name = 'posts/groups.html'
    context_object_name = 'posts'
    raise_exception = True

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['group_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title=context['posts'][0].category)
        return dict(list(context.items()) + list(mixin.items()))


class PostView(mixins.LoginRequiredMixin, DataMixin, DetailView, edit.FormMixin):
    context_object_name = 'post'
    template_name = 'posts/post.html'
    slug_url_kwarg = 'post_slug'
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse('post', kwargs={'post_slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.instance.comment_author = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        context['comments'] = self.object.comments.all()
        mixin = self.get_user_context(title=context['post'])
        count = self.cont_comment(slug=self.kwargs['post_slug'])
        return dict(list(context.items()) +
                    list(mixin.items()) + list(count.items()))


class About(DataMixin, TemplateView):
    template_name = 'posts/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='О нас')
        return dict(list(context.items()) + list(mixin.items()))


class Contact(DataMixin, TemplateView, edit.FormMixin):
    template_name = 'posts/contact.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(mixin.items()))


class RegisterUserView(DataMixin, CreateView):
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(mixin.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUserView(DataMixin, views.LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Войти')
        return dict(list(context.items()) + list(mixin.items()))

    def get_success_url(self) -> str:
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class AddPost(mixins.LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'posts/add_post.html'
    form_class = PostAddForm
    raise_exception = True

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(
            title='Добавить пост', 
            choice='Добавление поста поста'
        )
        return dict(list(context.items()) + list(mixin.items()))


def page_not_found(request, exception):
    return render(
        request,
        "errorclear/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    return render(request, "error/500.html", status=500)
    

def test(request):
    pass


class UpdatePost(mixins.LoginRequiredMixin, DataMixin, UpdateView):
    form_class = PostAddForm
    template_name = 'posts/edit.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    raise_exception = True

    def get_success_url(self) -> str:
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Рекдоктирование поста', choice='Редактирование поста')
        return dict(list(context.items()) + list(mixin.items()))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class DeletePost(mixins.LoginRequiredMixin,DataMixin, DeleteView):
    slug_url_kwarg = 'post_slug'
    template_name = 'posts/delete.html'
    raise_exception = True

    def get_success_url(self) -> str:
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin = self.get_user_context(title='Удаление поста ' + self.kwargs['post_slug'])
        return dict(list(context.items()) + list(mixin.items()))

