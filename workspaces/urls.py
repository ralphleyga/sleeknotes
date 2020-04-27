from django.urls import path

from .views import SlackHookReceiverView

app_name = 'workspaces'

urlpatterns = [
    path('hooks/receiver/', SlackHookReceiverView.as_view(), name='hook_receiver'),
]
