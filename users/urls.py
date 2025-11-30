from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AudioFileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'audio', AudioFileViewSet, basename='audio')

urlpatterns = [
    path('', include(router.urls)),
]
