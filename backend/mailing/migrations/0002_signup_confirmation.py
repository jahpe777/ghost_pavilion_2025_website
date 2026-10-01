import uuid
from django.db import migrations, models


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
        # Assign unique UUIDs per row using PostgreSQL native function
        migrations.RunSQL(
            sql="UPDATE mailing_signup SET confirmation_token = gen_random_uuid() WHERE confirmation_token IS NULL",
            reverse_sql=migrations.RunSQL.noop,
        ),
        # Make NOT NULL and add unique constraint
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
        # Sync Django's migration state
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
