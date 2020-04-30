from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import SlackAuthProvider


urlpatterns = default_urlpatterns(SlackAuthProvider)
