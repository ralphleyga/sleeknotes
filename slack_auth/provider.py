from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.slack.provider import SlackProvider


class SlackAuthProvider(SlackProvider):
    id = 'slack_auth'

    def get_default_scope(self):
        return []


provider_classes = [SlackAuthProvider]
