import asyncio
from slack import WebClient

from allauth.socialaccount.models import (
    SocialApp,
    SocialToken
    )

from .models import (
    WorkSpace,
    WorkSpaceChannel,
    Note,
    WorkSpaceUser,
    )

class SlackHelper(object):

    def initalize_slack_token(self, slack_token=''):
        self.client = WebClient(token=slack_token, run_async=True)

    def post_message(self, username, channel, text):
        """Post message as bot
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        message = f'<@{username}> posted {text}'
        chat = self.client.chat_postMessage(
                channel=channel,
                text=message)
        response = loop.run_until_complete(chat)
        return response
        
    def webhook_send(self, data):
        pass
    
    def initialize_workspace(self, user):
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

    def get_workspace(self, data):
        team_id = data['team_id']
        name = data['team_domain']
        domain = data['team_domain']
        workspace = WorkSpace.objects.get(team_id=team_id, domain=domain, name=name)
        return workspace
    
    def get_workspace_user(self, workspace, username):
        instance, created = WorkSpaceUser.objects.get_or_create(
            username=username,
            workspace=workspace
        )
        return instance

    def get_channel(self, workspace, data):
        name = data['channel_name']
        channel_id = data['channel_id']
        channel, created = WorkSpaceChannel.objects.get_or_create(
            workspace=workspace,
            name=name,
            channel_id=channel_id
        )
        return channel

    def create_note(self, channel, text, username):
        user = self.get_workspace_user(workspace=channel.workspace, username=username)

        instance, created = Note.objects.get_or_create(
            channel=channel,
            text=text,
            username=user
        )
        return instance

    def current_provider(self):
        return SocialApp.objects.get_current(provider='slack_auth')