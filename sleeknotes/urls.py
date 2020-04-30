"""sleeknotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users.views import IndexView, LoginView
from slack_auth.views import SlackLogin


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('slack_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/slack-auth/', SlackLogin.as_view(), name='slack_login'),

    path('workspaces/', include('workspaces.urls')),

    path('api/', include('workspaces.api_urls')),

    path('', IndexView.as_view(), name='index'),
    path('login/', IndexView.as_view(), name='slack_login'),
]
