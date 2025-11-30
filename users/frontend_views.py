from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Home page view"""
    template_name = 'home.html'


class UserDetailView(TemplateView):
    """User detail page view"""
    template_name = 'user_detail.html'
