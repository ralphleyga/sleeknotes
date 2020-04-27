from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .helpers import SlackHelper


@method_decorator(csrf_exempt, name='dispatch')
class SlackHookReceiverView(SlackHelper, View):

    def post(self, request, **kwargs):
        data = request.POST
        # get the stored token

        workspace = self.get_workspace(data)
        channel = self.get_channel(workspace, data)
        note = self.create_note(channel=channel, text=data['text'], username=data['user_name'])
        slack_token = workspace.active_token()
        self.initalize_slack_token(slack_token=slack_token)
        self.post_message(
            channel=note.channel.name,
            text=note.text,
            username=note.username.username
        )
        return HttpResponse('')