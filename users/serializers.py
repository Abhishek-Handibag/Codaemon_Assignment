from rest_framework import serializers
from .models import User, AudioFile


class AudioFileSerializer(serializers.ModelSerializer):
    """Serializer for AudioFile model"""
    file_size_display = serializers.CharField(source='get_file_size_display', read_only=True)
    audio_url = serializers.SerializerMethodField()

    class Meta:
        model = AudioFile
        fields = ['id', 'title', 'description', 'audio_file', 'audio_url', 
                  'duration', 'file_size', 'file_size_display', 
                  'uploaded_at', 'updated_at', 'is_active']
        read_only_fields = ['id', 'file_size', 'uploaded_at', 'updated_at']

    def get_audio_url(self, obj):
        request = self.context.get('request')
        if obj.audio_file and request:
            return request.build_absolute_uri(obj.audio_file.url)
        return None


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model with audio files"""
    audio_files = AudioFileSerializer(many=True, read_only=True)
    audio_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'bio', 'phone', 'created_at', 'updated_at', 
                  'audio_files', 'audio_count']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_audio_count(self, obj):
        return obj.audio_files.filter(is_active=True).count()


class UserBasicSerializer(serializers.ModelSerializer):
    """Basic user serializer without audio files"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                  'bio', 'phone', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
