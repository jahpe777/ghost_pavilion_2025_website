import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        # Grandfather existing subscribers as confirmed
        migrations.AddField(
            model_name='signup',
            name='is_confirmed',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='confirmation_token',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        # New signups default to not subscribed until confirmed
        migrations.AlterField(
            model_name='signup',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
