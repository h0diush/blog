from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<slug:post_slug>/', PostView.as_view(), name='post'),
    path('category/<slug:group_slug>/', ShowGroup.as_view(), name='group'),
    path('about/', About.as_view(), name='about'),
    path('add/', AddPost.as_view(), name='add_post'),
    path('contact/', Contact.as_view(), name='contact'),
    path('users/register/', RegisterUserView.as_view(), name='register'),
    path('users/login/', LoginUserView.as_view(), name='login'),
    path('users/logout/', logout_user, name='logout'),
    path('post/update/<slug:post_slug>/', UpdatePost.as_view(), name='update'),
    path('post/delete/<slug:post_slug>', DeletePost.as_view(), name='delete'),
    path('user/<slug:username>', UserView.as_view(), name='user'),
    path('post/<slug:post_slug>/like', like, name='like'),
    path('post/<slug:post_slug>/dislike', dislike, name='dislike'),
]
