from django.urls import path
from .frontend_views import HomeView, UserDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
]
