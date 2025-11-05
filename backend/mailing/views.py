from rest_framework import generics
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from .models import SignUp
from .serializers import SignUpSerializer
from django.http import JsonResponse

class SignUpCreateView(generics.CreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        print("Received data:", request.data)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Validation errors:", serializer.errors)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Save the new SignUp instance
        sign_up_instance = serializer.save()

        # Send a welcome email via SendGrid
        self.send_welcome_email(sign_up_instance.email)

    def send_welcome_email(self, recipient_email):
        # Construct the HTML email template
        html_content = """
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
                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: rgba(0, 0, 0, 0.7); border-radius: 8px; overflow: hidden;">
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
                                <td style="padding: 40px 30px; color: #ffffff; font-family: Verdana, Arial, sans-serif; text-align: center;">
                                    <h2 style="margin: 0 0 20px 0; color: #ff6600; font-size: 24px; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; font-family: Verdana, Arial, sans-serif;">
                                        WELCOME TO THE PAVILION
                                    </h2>

                                    <p style="margin: 0 0 20px 0; color: #ffffff; font-size: 16px; line-height: 1.6; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        Thank you for joining the Ghost Pavilion mailing list!
                                    </p>

                                    <p style="margin: 0 0 20px 0; color: #cccccc; font-size: 16px; line-height: 1.6; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        You're now part of our inner circle. Here's what you can expect from us:
                                    </p>

                                    <ul style="margin: 0 0 20px 0; padding: 0; list-style: none; color: #ffffff; font-size: 16px; line-height: 1.8; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        <li style="margin-bottom: 10px;">🎵 Early access to new releases</li>
                                        <li style="margin-bottom: 10px;">🎟️ Show announcements and exclusive ticket access</li>
                                        <li style="margin-bottom: 10px;">👕 Special discounts on merch drops</li>
                                        <li style="margin-bottom: 10px;">🎬 Behind-the-scenes content and music videos</li>
                                        <li style="margin-bottom: 10px;">✨ Exclusive updates you won't find anywhere else</li>
                                    </ul>

                                    <p style="margin: 20px 0 0 0; color: #cccccc; font-size: 16px; line-height: 1.6; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        Stay tuned for our next release coming soon.
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td style="padding: 30px; text-align: center; background-color: rgba(0, 0, 0, 0.5); border-top: 2px solid #ff6600;">
                                    <p style="margin: 0 0 10px 0; color: #999999; font-size: 12px; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        GHOST PAVILION © 2025
                                    </p>
                                    <p style="margin: 0; color: #999999; font-size: 12px; letter-spacing: 1px; font-family: Verdana, Arial, sans-serif;">
                                        <a href="https://ghostpavilion.com" style="color: #ff6600; text-decoration: none;">ghostpavilion.com</a>
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

        # Construct the email message
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=recipient_email,
            subject='Welcome to Ghost Pavilion',
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(f"Email sent to {recipient_email} with status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending email: {e}")
