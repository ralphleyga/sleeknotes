import json

from django.db import models
from django.conf import settings
from django.dispatch import receiver

from allauth.socialaccount.signals import social_account_updated
from allauth.socialaccount.models import SocialAccount


class WorkSpace(models.Model):
    name = models.CharField(max_length=200, unique=True)
    team_id = models.CharField(max_length=200, unique=True)
    domain = models.CharField(max_length=200, unique=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    social_account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def active_token(self):
        return self.social_account.socialtoken_set.all().first().token


class WorkSpaceChannel(models.Model):
    name = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=200)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Channel'

    def __str__(self):
        return f'{self.name} - {self.workspace.name}'


class WorkSpaceUser(models.Model):
    # We need model user for anonymouse users
    username = models.CharField(max_length=200) # username of user from slack
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.workspace.name} - {self.username}'
    
    class Meta:
        unique_together = ('username', 'user', 'workspace')


class Note(models.Model):
    channel = models.ForeignKey(WorkSpaceChannel, on_delete=models.CASCADE)
    text = models.TextField()
    username = models.ForeignKey(WorkSpaceUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.channel} - {self.username}'
