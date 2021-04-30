from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'users', UserApiView)
router.register(r'posts', PostApiView)
router.register(r'groups', CategoryApiView)

urlpatterns = [
    path('', include(router.urls))
]
