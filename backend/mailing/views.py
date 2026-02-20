from rest_framework import generics
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings
from .models import SignUp
from .serializers import SignUpSerializer
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class SignUpCreateView(generics.CreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        print("Received data:", request.data)
        email = request.data.get('email', '').lower().strip()
        name = request.data.get('name', '')

        # Check if email already exists (including unsubscribed users)
        try:
            existing_user = SignUp.objects.get(email=email)
            # If they were unsubscribed, re-subscribe them
            if not existing_user.is_subscribed:
                existing_user.is_subscribed = True
                existing_user.name = name  # Update name in case it changed
                existing_user.save()
                self.send_welcome_email(email, existing_user.unsubscribe_token)
                return JsonResponse({
                    'message': 'Welcome back! You have been re-subscribed.',
                    'email': email
                }, status=200)
            else:
                # Already subscribed
                return JsonResponse({
                    'message': 'You are already subscribed!',
                    'email': email
                }, status=200)
        except SignUp.DoesNotExist:
            # New user, proceed with normal creation
            pass

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("Validation errors:", serializer.errors)
            return JsonResponse({
                'error': 'Invalid data',
                'details': serializer.errors
            }, status=400)

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Save the new SignUp instance
        sign_up_instance = serializer.save()

        # Send a welcome email via SendGrid
        self.send_welcome_email(sign_up_instance.email, sign_up_instance.unsubscribe_token)

    def send_welcome_email(self, recipient_email, unsubscribe_token):
        # Build unsubscribe URL
        unsubscribe_url = f"https://ghostpavilion2025-production.up.railway.app/unsubscribe/{unsubscribe_token}/"

        # Construct the HTML email template
        html_content = f"""
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


class UnsubscribeView(View):
    """Handle unsubscribe requests via GET (clicked from email link)"""

    def get(self, request, token):
        try:
            subscriber = get_object_or_404(SignUp, unsubscribe_token=token)
            subscriber.is_subscribed = False
            subscriber.save()

            # Return a styled confirmation page
            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Unsubscribed - Ghost Pavilion</title>
            </head>
            <body style="margin: 0; padding: 0; font-family: Verdana, Arial, sans-serif; background: linear-gradient(135deg, #ff00ff, #ff0033, #ff6600, #ff0080); min-height: 100vh; display: flex; align-items: center; justify-content: center;">
                <div style="max-width: 500px; margin: 40px auto; padding: 40px; background-color: rgba(0, 0, 0, 0.8); border-radius: 8px; text-align: center;">
                    <h1 style="color: #ffffff; font-size: 28px; font-weight: bold; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 20px;">
                        GHOST PAVILION
                    </h1>
                    <p style="color: #ffffff; font-size: 18px; margin-bottom: 20px;">
                        You've been unsubscribed.
                    </p>
                    <p style="color: #cccccc; font-size: 14px; margin-bottom: 30px;">
                        We're sorry to see you go. You will no longer receive emails from us.
                    </p>
                    <a href="https://ghostpavilion.com" style="display: inline-block; background: linear-gradient(135deg, #ff0080, #ff6600); color: #ffffff; padding: 12px 30px; font-size: 14px; font-weight: bold; text-decoration: none; border-radius: 4px; letter-spacing: 2px; text-transform: uppercase;">
                        VISIT WEBSITE
                    </a>
                </div>
            </body>
            </html>
            """
            return HttpResponse(html_content)

        except Exception as e:
            return HttpResponse("Invalid unsubscribe link.", status=400)


@method_decorator(csrf_exempt, name='dispatch')
class SendMassEmailView(View):
    """Protected endpoint to trigger the music video mass email send."""

    ADMIN_KEY = "gp-mv-send-2026"

    def get(self, request):
        key = request.headers.get('X-Admin-Key', '')
        if key != self.ADMIN_KEY:
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        return JsonResponse({'subject': '\u201cNo Way to Love\u201d out now!', 'body': '\u201cNo Way to Love\u201d is out today!', 'button': 'LISTEN NOW'})

    def post(self, request):
        # Verify secret key
        key = request.headers.get('X-Admin-Key', '')
        if key != self.ADMIN_KEY:
            return JsonResponse({'error': 'Unauthorized'}, status=403)

        listen_url = "https://link.ghostpavilion.com/no-way-to-love"
        subject = "\u201cNo Way to Love\u201d out now!"

        subscribers = SignUp.objects.filter(is_subscribed=True)
        total = subscribers.count()
        sent = 0
        failed = 0
        errors = []

        for subscriber in subscribers:
            unsubscribe_url = f"https://ghostpavilion2025-production.up.railway.app/unsubscribe/{subscriber.unsubscribe_token}/"

            html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;font-family:Verdana,Arial,sans-serif;background:linear-gradient(135deg,#ff00ff,#ff0033,#ff6600,#ff0080);">
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin:0;padding:0;">
    <tr><td style="padding:40px 20px;">
      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width:600px;margin:0 auto;background-color:rgba(0,0,0,0.85);border-radius:8px;overflow:hidden;">
        <tr><td style="padding:40px 30px;text-align:center;background:linear-gradient(135deg,rgba(255,0,255,0.3),rgba(255,0,51,0.3),rgba(255,102,0,0.3));">
          <h1 style="margin:0;color:#ffffff;font-size:36px;font-weight:bold;letter-spacing:4px;text-transform:uppercase;font-family:'Impact','Arial Black',Verdana,sans-serif;">GHOST PAVILION</h1>
        </td></tr>
        <tr><td style="padding:40px 30px;color:#ffffff;font-family:Verdana,Arial,sans-serif;font-size:16px;line-height:1.8;">
          <p style="margin:0 0 25px 0;">\u201cNo Way to Love\u201d is out today!</p>
          <p style="margin:0 0 25px 0;text-align:center;">
            <a href="{listen_url}" style="display:inline-block;background:linear-gradient(135deg,#ff0080,#ff6600);color:#ffffff;padding:14px 32px;font-size:14px;font-weight:bold;text-decoration:none;border-radius:4px;letter-spacing:2px;text-transform:uppercase;">LISTEN NOW</a>
          </p>
          <p style="margin:0;">Thank you for being here and for supporting Ghost Pavilion.</p>
        </td></tr>
        <tr><td style="padding:30px;text-align:center;background-color:rgba(0,0,0,0.5);border-top:2px solid #ff6600;">
          <p style="margin:0 0 10px 0;color:#999999;font-size:12px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">GHOST PAVILION &copy; 2026</p>
          <p style="margin:0 0 10px 0;color:#999999;font-size:12px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">
            <a href="https://ghostpavilion.com" style="color:#ff6600;text-decoration:none;">ghostpavilion.com</a>
          </p>
          <p style="margin:0;color:#666666;font-size:10px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">
            <a href="{unsubscribe_url}" style="color:#666666;text-decoration:underline;">Unsubscribe</a>
          </p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""

            try:
                message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=subscriber.email,
                    subject=subject,
                    html_content=html
                )
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                if response.status_code == 202:
                    sent += 1
                else:
                    failed += 1
                    errors.append(f"{subscriber.email}: status {response.status_code}")
            except Exception as e:
                failed += 1
                errors.append(f"{subscriber.email}: {str(e)}")

        return JsonResponse({
            'total': total,
            'sent': sent,
            'failed': failed,
            'errors': errors
        })
