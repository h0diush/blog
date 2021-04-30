from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from blog.models import *

from .permissions import *
from .serializers import *
from .filterset import *


class UserApiView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserApiSerializer
    permission_classes = [permissions.IsAuthenticated, UserPermission]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated, PostPermission]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return PostApiCreateSerializer
        return PostApiSerializer


class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryApiSerializer
    permission_classes = [permissions.IsAuthenticated, CategoryPermission]
