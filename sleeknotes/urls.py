from django.contrib import admin
from django.urls import path, include

from users.views import IndexView, LoginView
from slack_auth.views import SlackLogin


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('slack_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/rest-auth/slack-auth/', SlackLogin.as_view(), name='slack_rest_login'),

    path('workspaces/', include('workspaces.urls')),
    path('login/', LoginView.as_view(), name='slack_login'),
    path('api/', include('workspaces.api_urls')),
    
    path('', include('users.urls')),
]
