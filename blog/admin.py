from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'slug',
        'author',
        'content',
        'pub_date',
        'category',
        'image',
        'tags')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('pub_date',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title',)
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'avatar')
    search_fields = ('username',)
    list_display_links = ('username',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'text')
    search_fields = ('name', 'email', 'subject')
    list_display_links = ('name', 'email')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
