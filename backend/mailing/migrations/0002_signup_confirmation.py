import uuid
from django.db import migrations, models


def populate_confirmation_tokens(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    SignUp = apps.get_model('mailing', 'SignUp')
    for signup in SignUp.objects.using(db_alias).filter(confirmation_token__isnull=True):
        signup.confirmation_token = uuid.uuid4()
        signup.save(update_fields=['confirmation_token'])


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        # Add is_confirmed — existing subscribers grandfathered as True
        migrations.RunSQL(
            sql="ALTER TABLE mailing_signup ADD COLUMN IF NOT EXISTS is_confirmed boolean NOT NULL DEFAULT true",
            reverse_sql="ALTER TABLE mailing_signup DROP COLUMN IF EXISTS is_confirmed",
        ),
        # Add confirmation_token as nullable first (no unique constraint yet)
        migrations.RunSQL(
            sql="ALTER TABLE mailing_signup ADD COLUMN IF NOT EXISTS confirmation_token uuid NULL",
            reverse_sql="ALTER TABLE mailing_signup DROP COLUMN IF EXISTS confirmation_token",
        ),
        # Assign a unique UUID to every existing row
        migrations.RunPython(populate_confirmation_tokens, migrations.RunPython.noop),
        # Now make it NOT NULL and unique
        migrations.RunSQL(
            sql="""
                ALTER TABLE mailing_signup ALTER COLUMN confirmation_token SET NOT NULL;
                DO $$ BEGIN
                    ALTER TABLE mailing_signup ADD CONSTRAINT mailing_signup_confirmation_token_key UNIQUE (confirmation_token);
                EXCEPTION WHEN duplicate_table THEN NULL;
                END $$;
            """,
            reverse_sql="ALTER TABLE mailing_signup DROP CONSTRAINT IF EXISTS mailing_signup_confirmation_token_key",
        ),
        # Change is_subscribed default to False for new signups
        migrations.RunSQL(
            sql="ALTER TABLE mailing_signup ALTER COLUMN is_subscribed SET DEFAULT false",
            reverse_sql="ALTER TABLE mailing_signup ALTER COLUMN is_subscribed SET DEFAULT true",
        ),
        # Sync Django's migration state tracker
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.AddField(
                    model_name='signup',
                    name='is_confirmed',
                    field=models.BooleanField(default=False),
                ),
                migrations.AddField(
                    model_name='signup',
                    name='confirmation_token',
                    field=models.UUIDField(default=uuid.uuid4, unique=True),
                ),
                migrations.AlterField(
                    model_name='signup',
                    name='is_subscribed',
                    field=models.BooleanField(default=False),
                ),
            ],
        ),
    ]
