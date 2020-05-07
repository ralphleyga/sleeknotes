from django.utils.timesince import timesince
from rest_framework import serializers

from .models import (
        Note,
        WorkSpace,
        WorkSpaceChannel,
        WorkSpaceUser,
    )


class NoteSerializer(serializers.ModelSerializer):
    channel = serializers.SerializerMethodField()
    workspace = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = '__all__'
        
    def get_channel(self, instance):
        serializer = WorkspaceChannelSerializer(instance=instance.channel)
        return serializer.data
    
    def get_workspace(self, instance):
        return WorkSpaceSerializer(instance.channel.workspace).data
    
    def get_created(self, instance):
        return timesince(instance.created)


class WorkSpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSpace
        fields = ('id', 'name', 'domain')


class WorkSpaceMemberSerializer(WorkSpaceSerializer):
    users = serializers.SerializerMethodField()

    def get_users(self, instance):
        serializer = WorkspaceUserSerializer(instance.workspaceuser_set.all(), many=True)
        return serializer.data
    
    class Meta:
        model = WorkSpace
        fields = ('id', 'name', 'domain', 'users')


class WorkspaceChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaceChannel
        fields = '__all__'


class WorkspaceUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpaceUser
        fields = '__all__'
