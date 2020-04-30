from rest_framework import serializers

from .models import (
        Note,
        WorkSpace,
        WorkSpaceChannel,
    )


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class WorkSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = ('id', 'name', 'domain')


class WorkspaceChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaceChannel
        fields = '__all__'
