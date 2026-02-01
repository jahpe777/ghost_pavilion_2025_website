from django.core.management.base import BaseCommand
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from mailing.models import SignUp


class Command(BaseCommand):
    help = 'Send a mass email to all subscribers'

    def add_arguments(self, parser):
        parser.add_argument('subject', type=str, help='Email subject line')
        parser.add_argument('message', type=str, help='Email message content (can be HTML)')
        parser.add_argument('--preview', action='store_true', help='Preview emails without sending')

    def handle(self, *args, **options):
        subject = options['subject']
        message_content = options['message']
        preview_mode = options['preview']

        # Get all active subscribers (is_subscribed=True)
        subscribers = SignUp.objects.filter(is_subscribed=True)
        total_subscribers = subscribers.count()

        if total_subscribers == 0:
            self.stdout.write(self.style.WARNING('No subscribers found!'))
            return

        self.stdout.write(self.style.SUCCESS(f'Found {total_subscribers} subscribers'))

        if preview_mode:
            self.stdout.write(self.style.WARNING('\n=== PREVIEW MODE - No emails will be sent ===\n'))
            self.stdout.write(f'Subject: {subject}\n')
            self.stdout.write(f'Message preview:\n{message_content[:200]}...\n')
            self.stdout.write(f'\nWould send to: {", ".join([s.email for s in subscribers[:5]])}...')
            return

        # Confirm before sending
        confirm = input(f'\nSend email to {total_subscribers} subscribers? (yes/no): ')
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.WARNING('Cancelled.'))
            return

        # Build HTML template
        html_content = self._build_email_template(message_content)

        # Send emails
        sent_count = 0
        failed_count = 0

        for subscriber in subscribers:
            try:
                # Build personalized email with unsubscribe link
                personalized_html = self._build_email_template(message_content, subscriber.unsubscribe_token)

                message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=subscriber.email,
                    subject=subject,
                    html_content=personalized_html
                )

                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)

                if response.status_code == 202:
                    sent_count += 1
                    self.stdout.write(f'✓ Sent to {subscriber.email}')
                else:
                    failed_count += 1
                    self.stdout.write(self.style.WARNING(f'✗ Failed to send to {subscriber.email} (status: {response.status_code})'))

            except Exception as e:
                failed_count += 1
                self.stdout.write(self.style.ERROR(f'✗ Error sending to {subscriber.email}: {str(e)}'))

        # Summary
        self.stdout.write(self.style.SUCCESS(f'\n=== Summary ==='))
        self.stdout.write(self.style.SUCCESS(f'Sent: {sent_count}'))
        if failed_count > 0:
            self.stdout.write(self.style.WARNING(f'Failed: {failed_count}'))

    def _build_email_template(self, message_content, unsubscribe_token):
        """Build the HTML email template matching Ghost Pavilion style with unsubscribe link"""
        # Use the backend API URL for unsubscribe
        unsubscribe_url = f"https://ghostpavilion2025-production.up.railway.app/unsubscribe/{unsubscribe_token}/"

        # Pre-save link
        presave_url = "https://distrokid.com/hyperfollow/ghostpavilion/no-way-to-love"

        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="margin: 0; padding: 0; font-family: Verdana, Arial, sans-serif; background: linear-gradient(135deg, #ff00ff, #ff0033, #ff6600, #ff0080); background-size: 200% 200%;">
            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin: 0; padding: 0;">
                <tr>
                    <td style="padding: 40px 20px;">
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: rgba(0, 0, 0, 0.85); border-radius: 8px; overflow: hidden;">
                            <!-- Header -->
                            <tr>
                                <td style="padding: 40px 30px; text-align: center; background: linear-gradient(135deg, rgba(255, 0, 255, 0.3), rgba(255, 0, 51, 0.3), rgba(255, 102, 0, 0.3));">
                                    <h1 style="margin: 0; color: #ffffff; font-size: 36px; font-weight: bold; letter-spacing: 4px; text-transform: uppercase; font-family: 'Impact', 'Arial Black', Verdana, sans-serif;">
                                        GHOST PAVILION
                                    </h1>
                                </td>
                            </tr>

                            <!-- Main Content -->
                            <tr>
                                <td style="padding: 40px 30px; color: #ffffff; font-family: Verdana, Arial, sans-serif; font-size: 16px; line-height: 1.8;">
                                    <p style="margin: 0 0 25px 0;">
                                        I wanted to share something I have been working on with you.
                                    </p>

                                    <p style="margin: 0 0 25px 0;">
                                        My new single, <strong>No Way to Love</strong>, drops on <strong>February 20th</strong>.
                                    </p>

                                    <p style="margin: 0 0 25px 0;">
                                        You can pre save it now so it is waiting for you the moment it goes live.
                                    </p>

                                    <p style="margin: 0 0 25px 0;">
                                        <a href="{presave_url}" style="color: #ff6600; font-weight: bold; text-decoration: none; text-transform: uppercase; letter-spacing: 2px;">PRE SAVE NOW</a>
                                    </p>

                                    <p style="margin: 0 0 25px 0;">
                                        As a thank you for being on the mailing list, you will also receive the music video ahead of the public release as a special bonus.
                                    </p>

                                    <p style="margin: 0 0 25px 0;">
                                        Thank you for being here and for supporting Ghost Pavilion. You are part of the core group behind this project, and you will continue to receive early updates, releases, and behind the scenes moments moving forward.
                                    </p>

                                    <p style="margin: 0 0 25px 0;">
                                        I truly appreciate you being here.
                                    </p>

                                    <p style="margin: 0;">
                                        – Ghost Pavilion
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td style="padding: 30px; text-align: center; background-color: rgba(0, 0, 0, 0.5); border-top: 2px solid #ff6600;">
                                    <p style="margin: 0 0 10px 0; color: #999999; font-size: 12px; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        GHOST PAVILION © 2025
                                    </p>
                                    <p style="margin: 0 0 10px 0; color: #999999; font-size: 12px; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        <a href="https://ghostpavilion.com" style="color: #ff6600; text-decoration: none;">ghostpavilion.com</a>
                                    </p>
                                    <p style="margin: 0; color: #666666; font-size: 10px; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        <a href="{unsubscribe_url}" style="color: #666666; text-decoration: underline;">Unsubscribe</a>
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
