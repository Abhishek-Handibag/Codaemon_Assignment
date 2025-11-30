from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.shortcuts import get_object_or_404
from .models import User, AudioFile
from .serializers import UserSerializer, UserBasicSerializer, AudioFileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User operations
    Provides list, retrieve, create, update, delete operations
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['list', 'create', 'update', 'partial_update']:
            return UserBasicSerializer
        return UserSerializer

    @action(detail=True, methods=['get'])
    def audio_files(self, request, pk=None):
        """Get all audio files for a specific user"""
        user = self.get_object()
        audio_files = user.audio_files.filter(is_active=True)
        serializer = AudioFileSerializer(audio_files, many=True, context={'request': request})
        return Response(serializer.data)


class AudioFileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for AudioFile operations
    Provides list, retrieve, create, update, delete operations
    """
    queryset = AudioFile.objects.filter(is_active=True)
    serializer_class = AudioFileSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_context(self):
        """Ensure request context is passed to serializer"""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        """Filter audio files by user if user_id is provided"""
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def create(self, request, *args, **kwargs):
        """Upload a new audio file for a user"""
        user_id = request.data.get('user_id')
        if not user_id:
            return Response(
                {'error': 'user_id is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        user = get_object_or_404(User, id=user_id)
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Update an existing audio file"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Soft delete audio file by setting is_active to False"""
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {'message': 'Audio file deleted successfully'}, 
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=True, methods=['delete'])
    def hard_delete(self, request, pk=None):
        """Permanently delete audio file and remove from storage"""
        audio_file = self.get_object()
        audio_file.delete()
        return Response(
            {'message': 'Audio file permanently deleted'}, 
            status=status.HTTP_204_NO_CONTENT
        )
