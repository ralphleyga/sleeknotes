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
        self.slack_token = self.current_provider().key
        workspace = self.get_workspace(data)
        import pdb; pdb.set_trace()
        channel = self.get_channel(workspace, data)
        note = self.create_note(channel=channel, text=data['text'], username=data['user_name'])
        
        message = 'note successfully posted'
        return HttpResponse(message)