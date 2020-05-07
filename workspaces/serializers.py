from rest_framework import serializers

from .models import (
        Note,
        WorkSpace,
        WorkSpaceChannel,
    )


class NoteSerializer(serializers.ModelSerializer):
    channel = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = '__all__'
        
    def get_channel(self, instance):
        serializer = WorkspaceChannelSerializer(instance=instance.channel)
        return serializer.data


class WorkSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = ('id', 'name', 'domain')


class WorkspaceChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaceChannel
        fields = '__all__'
