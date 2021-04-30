from rest_framework.permissions import SAFE_METHODS, BasePermission

from blog.models import Role


class PostPermission(BasePermission):
    def has_obj_permission(self, request, view):
        return (
            request.method in
            SAFE_METHODS or request.user
            and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.method in [
            'PATCH',
            'DELETE',
            'PUT'
        ] and obj.author == request.user or request.user.role == Role.ADMIN:
            return True


class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
                request.user.role == Role.ADMIN or request.user.role == Role.MODERATOR) or request.method == 'GET':
            return True
        return False


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == Role.ADMIN or request.method == 'GET':
            return True
        return False
