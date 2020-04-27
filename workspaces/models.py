import json

from django.db import models
from django.conf import settings
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_updated


class WorkSpace(models.Model):
    name = models.CharField(max_length=200, unique=True)
    team_id = models.CharField(max_length=200, unique=True)
    domain = models.CharField(max_length=200, unique=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class WorkSpaceChannel(models.Model):
    name = models.CharField(max_length=200)
    channel_id = models.CharField(max_length=200)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.workspace.name}'


class WorkSpaceUser(models.Model):
    username = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING)
    workspace = models.ForeignKey(WorkSpace, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} - {self.username}'
    
    class Meta:
        unique_together = ('username', 'user')


class Note(models.Model):
    channel = models.ForeignKey(WorkSpaceChannel, on_delete=models.CASCADE)
    text = models.TextField()
    username = models.ForeignKey(WorkSpaceUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.channel} - {self.username}'


@receiver(social_account_updated)
def update_user_workspace(sender, **kwargs):
    user = kwargs['request'].user
    user_slacks = user.socialaccount_set.filter(provider='slack_auth')

    for user_slack in user_slacks:
        # initialize user workspace
        data = user_slack.extra_data
        team_id = data['team']['id']
        name = data['team']['name']
        domain = data['team']['domain']
        
        workspace, created = WorkSpace.objects.get_or_create(
            user=user,
            name=name,
            domain=domain,
            team_id=team_id
        )
