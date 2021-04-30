from blog.models import Category, Role, UserProfile
import django_filters as filters

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок поста'
    )
    category = filters.ModelChoiceFilter(
        queryset=Category.objects.all()
    )
    author = filters.CharFilter(
        field_name='author__username',
        lookup_expr='icontains',
        label='Автор поста'
    )
    pub_date = filters.DateRangeFilter()


class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название категории'
    )
    slug = filters.CharFilter(
        field_name='slug',
        lookup_expr='exact',
        label='URL'
    )


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(
        field_name='username',
        lookup_expr='icontains',
        label='Имя пользователя',
    )
    role = filters.ChoiceFilter(choices=Role.choices)