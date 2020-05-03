from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
        WorkSpace,
        WorkSpaceChannel,
        Note
    )

from .serializers import (
        WorkSpaceSerializer,
        WorkspaceChannelSerializer,
        NoteSerializer
    )


class AllNotesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all().order_by('-created')
    serializer_class = NoteSerializer
    filter_backend = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('channel', 'text')
    
    def get_queryset(self):
        return super().get_queryset().filter(username__workspace__user=self.request.user)


class WorkSpaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkSpace.objects.all().order_by('-created')
    serializer_class = WorkSpaceSerializer
