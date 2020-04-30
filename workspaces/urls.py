from django.urls import path

from .views import SlackHookNoteView

app_name = 'workspaces'

urlpatterns = [
    path('hooks/note/', SlackHookNoteView.as_view(), name='hook_note'),
]
