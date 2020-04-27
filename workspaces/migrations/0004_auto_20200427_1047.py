# Generated by Django 3.0.5 on 2020-04-27 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspaces', '0003_auto_20200427_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspaceuser',
            name='workspace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='workspaces.WorkSpace'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='workspaceuser',
            unique_together={('username', 'user')},
        ),
    ]
