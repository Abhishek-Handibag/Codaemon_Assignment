from django.contrib import admin
from .models import User, AudioFile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['created_at']


@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'get_file_size_display', 'is_active', 'uploaded_at']
    search_fields = ['title', 'user__username', 'description']
    list_filter = ['is_active', 'uploaded_at']
    readonly_fields = ['file_size', 'uploaded_at', 'updated_at']
