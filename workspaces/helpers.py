from slack import WebClient

from allauth.socialaccount.models import (
    SocialApp,
    SocialToken
    )

from .models import (
    WorkSpace,
    WorkSpaceChannel,
    Note,
    )

class SlackHelper(object):
    slack_token = ''

    def __init__(self):
        self.client = WebClient(token=self.slack_token)

    def post_message(self, channel, text):
        """Post message as bot
        """
        return self.client.chat_postMessage(
                channel=channel,
                text=text)
        
    def webhook_send(self, data):
        pass

    def get_workspace(self, data):
        team_id = data['team_id']
        name = data['team_domain']
        domain = data['team_domain']
        workspace = WorkSpace.objects.get(team_id=team_id, domain=domain, name=name)
        return workspace

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
        return Note.objects.get_or_create(
            channel=channel,
            text=text,
            username=username
        )
        
    def current_provider(self):
        return SocialApp.objects.get_current(provider='slack_auth')