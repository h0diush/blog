from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from taggit.forms import TagField

from .models import UserProfile
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'name': "name",
                'type': "text",
                'id': "name",
                'placeholder': "Ваше имя",
                'required': "",
            }
        )
    )

    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'name': "email",
                'type': "text",
                'id': "email",
                'placeholder': "Ваша электронная почта",
                'required': "",
            }
        )
    )

    subject = forms.CharField(
        label='Предмет',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'name': "subject",
                'type': "text",
                'id': "subject",
                'placeholder': "Предмет",
            }
        )
    )

    text = forms.CharField(
        label='Текст',
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'name': "message",
                'rows': "6",
                'id': "message",
                'placeholder': "Ваше сообщение",
                'required': "",
            }
        )
    )

    class Meta:
        model = Contact
        fields = '__all__'


class CommentForm(forms.ModelForm):
    pass


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя: ',
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "username",
                'placeholder': "Имя пользователя",
                'required': ""
            }
        )
    )
    email = forms.CharField(
        label='Электронная почта: ',
        widget=forms.TextInput(
            attrs={
                'type': "email",
                'class': "form-control",
                'id': "email",
                'placeholder': "you@example.com"
            }
        )
    )
    first_name = forms.CharField(
        label='Имя: ',
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "firstName",
                'placeholder': "",
                'value': "",
                'required': ""
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия: ',
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "lastName",
                'placeholder': "",
                'value': "",
                'required': ""
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль: ',
        widget=forms.PasswordInput(
            attrs={
                'type': "password",
                'class': "form-control",
                'id': "exampleInputPassword1",
                'placeholder': "Пароль"
            }
        )
    )
    password2 = forms.CharField(
        label='Пароль ещё раз: ',
        widget=forms.PasswordInput(
            attrs={
                'type': "password",
                'class': "form-control",
                'id': "exampleInputPassword1",
                'placeholder': "Ещё раз"
            }
        )
    )
    avatar = forms.ImageField(label='Аватар')

    class Meta:
        model = UserProfile
        fields = [
            'username',
            'email',
            'avatar',
            'first_name',
            'last_name',
            'password1',
            'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "username",
                'placeholder': "Имя пользователя",
                'required': ""
            }
        )
    )

    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'type': "password",
                'class': "form-control",
                'id': "exampleInputPassword1",
                'placeholder': "Пароль"
            }
        )
    )

    class Meta:
        model = UserProfile
        fields = ['username', 'password']


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label='Текст комментария',
        widget=forms.Textarea(
            attrs={
                'name': "message",
                'rows': "6",
                'id': "message",
                'placeholder': "Оставьте свой комментарий",
                'required': "",
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('text',)


class PostAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['category'].label = 'Категория'

    title = forms.CharField(
        label='Заголовок',
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "username",
                'placeholder': "Заголовок",
                'required': ""
            }
        )
    )

    slug = forms.CharField(
        label='URL',
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control",
                'id': "username",
                'placeholder': "Если не указать, сгенерируется автоматически",
            }
        ),
        required=False
    )

    content = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'name': "message",
                'rows': "6",
                'id': "message",
                'placeholder': "Описание",
                'required': "",
            }
        )
    )

    tags = TagField(
        label='Тэги',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Укажите через запятую",
                'name': 'tags',
                'data-role': 'tagsinput',
            }
        )
    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'tags', 'category', 'image', 'content']
