from django.db import models
from django.core.validators import FileExtensionValidator
import os


class User(models.Model):
    """User model to store user details"""
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username


def audio_upload_path(instance, filename):
    """Generate upload path for audio files"""
    return f'audio/{instance.user.username}/{filename}'


class AudioFile(models.Model):
    """Audio file model to store user's audio files"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audio_files')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    audio_file = models.FileField(
        upload_to=audio_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg', 'm4a', 'flac'])]
    )
    duration = models.FloatField(null=True, blank=True)  # Duration in seconds
    file_size = models.IntegerField(null=True, blank=True)  # Size in bytes
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def save(self, *args, **kwargs):
        """Override save to store file size"""
        if self.audio_file:
            self.file_size = self.audio_file.size
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Override delete to remove file from storage"""
        if self.audio_file:
            if os.path.isfile(self.audio_file.path):
                os.remove(self.audio_file.path)
        super().delete(*args, **kwargs)

    def get_file_size_display(self):
        """Return human-readable file size"""
        if self.file_size:
            size_mb = self.file_size / (1024 * 1024)
            if size_mb < 1:
                return f"{self.file_size / 1024:.2f} KB"
            return f"{size_mb:.2f} MB"
        return "Unknown"
