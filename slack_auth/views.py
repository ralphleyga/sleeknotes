import requests
import logging
logger = logging.getLogger(__name__)

from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import SlackNewProvider


from slack import WebClient


class SlackOAuth2Adapter(OAuth2Adapter):
    provider_id = SlackNewProvider.id

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


oauth2_login = OAuth2LoginView.adapter_view(SlackOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(SlackOAuth2Adapter)
