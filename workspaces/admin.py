from django.contrib import admin

from .models import (
    WorkSpace,
    WorkSpaceChannel,
    Note,
    WorkSpaceUser
)

class ChannelInline(admin.TabularInline):
    model = WorkSpaceChannel


class WorkSpaceUserInline(admin.TabularInline):
    model = WorkSpaceUser


@admin.register(WorkSpace)
class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'name', 'domain')

    inlines = [
        ChannelInline,
        WorkSpaceUserInline
    ]


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel', 'username', 'created')