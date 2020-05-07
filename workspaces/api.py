from rest_framework import viewsets, views
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

import logging
logger = logging.getLogger('onboarding')


from .models import (
        WorkSpace,
        WorkSpaceChannel,
        Note
    )

from .serializers import (
        WorkSpaceSerializer,
        WorkspaceChannelSerializer,
        WorkspaceUserSerializer,
        WorkSpaceMemberSerializer,
        NoteSerializer
    )


class AllNotesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all().order_by('-created')
    serializer_class = NoteSerializer
    filter_backend = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('channel', 'text')
    
    def get_queryset(self):
        logger.debug('Something went wrong!')
        return super().get_queryset().filter(username__workspace__workspaceuser__user=self.request.user).select_related('channel', 'channel__workspace')


class WorkSpaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkSpace.objects.all().order_by('-created')
    serializer_class = WorkSpaceMemberSerializer
