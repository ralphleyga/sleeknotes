import requests
import logging
logger = logging.getLogger(__name__)

from allauth.socialaccount.providers.oauth2.client import OAuth2Error, OAuth2Client
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from rest_auth.registration.views import SocialLoginView

from .provider import SlackAuthProvider


from slack import WebClient


class SlackOAuth2Adapter(OAuth2Adapter):
    provider_id = SlackAuthProvider.id
    identity_url = 'https://slack.com/api/users.identity'
    access_token_url = 'https://slack.com/api/oauth.v2.access'
    authorize_url = 'https://slack.com/oauth/v2/authorize'

    def complete_login(self, request, app, token, **kwargs):
        token = kwargs['response']['authed_user']['access_token']

        extra_data = self.get_data(token)
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)

    def get_data(self, token):
        resp = requests.get(
            self.identity_url,
            params={'token': token}
        )
        resp = resp.json()
        if not resp.get('ok'):
            raise OAuth2Error()

        return resp



class SlackLogin(SocialLoginView):
    adapter_class = SlackOAuth2Adapter
    callback_url = 'http://sleeknotes.test/accounts/slack_auth/login/callback/'
    client_class = OAuth2Client


oauth2_login = OAuth2LoginView.adapter_view(SlackOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(SlackOAuth2Adapter)

