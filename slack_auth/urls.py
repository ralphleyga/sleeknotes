from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import SlackNewProvider


urlpatterns = default_urlpatterns(SlackNewProvider)
