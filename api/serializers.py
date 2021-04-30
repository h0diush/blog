from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from blog.models import *


class FollowerApiSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only = True
    )
    class Meta:
        model = Follow
        fields = ['author']


class FollowingApiSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only = True
    )
    class Meta:
        model = Follow
        fields = ['user']
    

class UserApiSerializer(serializers.ModelSerializer):
    follower = FollowerApiSerializer(read_only=True, many=True)
    following = FollowingApiSerializer(read_only=True, many=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role', 'first_name', 'last_name', 'email', 'follower', 'following']


class LikeApiSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field = 'username', 
        read_only = True
    )
    class Meta:
        model = Like
        fields = ['user']


class CommentApiSerializer(serializers.ModelSerializer):
    comment_author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    class Meta:
        model = Comment
        fields = ['text', 'comment_author']


class CategoryApiSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(
        allow_blank=False,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        exclude = ['id']


class PostApiSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    category = CategoryApiSerializer(read_only=True)
    comments = CommentApiSerializer(many=True, read_only=True)
    likes = LikeApiSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'category', 'pub_date', 'comments', 'likes']


class PostApiCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'category', 'image']


class UserProfileApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name']
