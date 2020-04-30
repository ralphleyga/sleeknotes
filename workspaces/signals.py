from django.apps import apps
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_updated


@receiver(social_account_updated)
def update_user_workspace(sender, **kwargs):
    user = kwargs['request'].user
    user_slacks = user.socialaccount_set.filter(provider='slack_auth')
    WorkSpace = apps.get_model('workspaces', 'WorkSpace')
    WorkSpaceUser = apps.get_model('workspaces', 'WorkSpaceUser')

    for user_slack in user_slacks:
        # initialize user workspace
        data = user_slack.extra_data
        team_id = data['team']['id']
        name = data['team']['name']
        domain = data['team']['domain']

        workspace, created = WorkSpace.objects.get_or_create(
            user=user,
            name=name,
            domain=domain,
            team_id=team_id,
            social_account=user_slack
        )

        # create workspace user
        workspace_user, created = WorkSpaceUser.objects.get_or_create(
            workspace=workspace,
            username=data['user']['name']
        )

        # update if there's existing workspace_user to connec the user account
        workspace_user.user = user
        workspace_user.save()
