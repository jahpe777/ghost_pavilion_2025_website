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

        try:
            existing_user = SignUp.objects.get(email=email)
            if not existing_user.is_confirmed:
                # Resend confirmation email
                self.send_confirmation_email(existing_user.email, existing_user.confirmation_token)
                return JsonResponse({
                    'message': 'Please check your email to confirm your subscription.',
                    'email': email
                }, status=200)
            elif not existing_user.is_subscribed:
                existing_user.is_subscribed = True
                existing_user.name = name
                existing_user.save()
                return JsonResponse({
                    'message': 'Welcome back! You have been re-subscribed.',
                    'email': email
                }, status=200)
            else:
                return JsonResponse({
                    'message': 'You are already subscribed!',
                    'email': email
                }, status=200)
        except SignUp.DoesNotExist:
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
        sign_up_instance = serializer.save()
        self.send_confirmation_email(sign_up_instance.email, sign_up_instance.confirmation_token)

    def send_confirmation_email(self, recipient_email, confirmation_token):
        confirm_url = f"https://ghostpavilion2025-production.up.railway.app/confirm/{confirmation_token}/"

        html_content = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;font-family:Verdana,Arial,sans-serif;background-color:#ffffff;">
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin:0;padding:0;background-color:#ffffff;">
    <tr><td style="padding:40px 20px;">
      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width:600px;margin:0 auto;background-color:#ffffff;border-radius:8px;overflow:hidden;border:1px solid #e0e0e0;">
        <tr><td style="padding:40px 30px;text-align:center;background-color:#222222;">
          <h1 style="margin:0;color:#ffffff;font-size:36px;font-weight:bold;letter-spacing:4px;text-transform:uppercase;font-family:'Impact','Arial Black',Verdana,sans-serif;">GHOST PAVILION</h1>
        </td></tr>
        <tr><td style="padding:40px 30px;color:#222222;font-family:Verdana,Arial,sans-serif;font-size:16px;line-height:1.8;text-align:center;">
          <p style="margin:0 0 25px 0;text-align:center;">Thanks for signing up. Tap the button below to confirm your email and join the mailing list.</p>
          <p style="margin:0 0 25px 0;text-align:center;">
            <a href="{confirm_url}" style="display:inline-block;background-color:#222222;color:#ffffff;padding:14px 40px;font-size:14px;font-weight:bold;text-decoration:none;border-radius:4px;letter-spacing:2px;text-transform:uppercase;font-family:Verdana,Arial,sans-serif;">CONFIRM EMAIL</a>
          </p>
          <p style="margin:0;text-align:center;color:#888888;font-size:13px;">If you did not sign up for this, you can ignore this email.</p>
        </td></tr>
        <tr><td style="padding:30px;text-align:center;background-color:#f5f5f5;border-top:2px solid #222222;">
          <p style="margin:0 0 10px 0;color:#555555;font-size:12px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">GHOST PAVILION &copy; 2026</p>
          <p style="margin:0;color:#555555;font-size:12px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">
            <a href="https://ghostpavilion.com" style="color:#222222;text-decoration:none;">ghostpavilion.com</a>
          </p>
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>"""

        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=recipient_email,
            subject='Confirm your Ghost Pavilion subscription',
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(f"Confirmation email sent to {recipient_email}: {response.status_code}")
        except Exception as e:
            print(f"Error sending confirmation email: {e}")


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


class ConfirmEmailView(View):
    """Handle email confirmation via link clicked from confirmation email."""

    def get(self, request, token):
        try:
            subscriber = get_object_or_404(SignUp, confirmation_token=token)
            subscriber.is_confirmed = True
            subscriber.is_subscribed = True
            subscriber.save()

            html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmed - Ghost Pavilion</title>
</head>
<body style="margin:0;padding:0;font-family:Verdana,Arial,sans-serif;background-color:#ffffff;min-height:100vh;display:flex;align-items:center;justify-content:center;">
    <div style="max-width:500px;margin:40px auto;padding:40px;background-color:#ffffff;border:1px solid #e0e0e0;border-radius:8px;text-align:center;">
        <h1 style="color:#222222;font-size:28px;font-weight:bold;letter-spacing:4px;text-transform:uppercase;margin-bottom:20px;font-family:'Impact','Arial Black',Verdana,sans-serif;">
            GHOST PAVILION
        </h1>
        <p style="color:#222222;font-size:18px;margin-bottom:20px;">
            You are in.
        </p>
        <p style="color:#555555;font-size:14px;margin-bottom:30px;">
            Your email has been confirmed. You will receive updates on new music, videos, and releases.
        </p>
        <a href="https://ghostpavilion.com" style="display:inline-block;background-color:#222222;color:#ffffff;padding:12px 30px;font-size:14px;font-weight:bold;text-decoration:none;border-radius:4px;letter-spacing:2px;text-transform:uppercase;">
            VISIT WEBSITE
        </a>
    </div>
</body>
</html>"""
            return HttpResponse(html_content)

        except Exception as e:
            return HttpResponse("Invalid confirmation link.", status=400)


@method_decorator(csrf_exempt, name='dispatch')
class SendMassEmailView(View):
    """Protected endpoint to trigger the music video mass email send."""

    ADMIN_KEY = "gp-mv-send-2026"

    def get(self, request):
        key = request.headers.get('X-Admin-Key', '')
        if key != self.ADMIN_KEY:
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        subscribers = SignUp.objects.filter(is_subscribed=True, is_confirmed=True).values_list('name', 'email')
        return JsonResponse({
            'subject': 'Pre-save the new single, "Black Armor"',
            'body_preview': 'I have a new single coming out called Black Armor',
            'total': subscribers.count(),
            'subscribers': [{'name': n, 'email': e} for n, e in subscribers]
        })

    def post(self, request):
        import json
        key = request.headers.get('X-Admin-Key', '')
        if key != self.ADMIN_KEY:
            return JsonResponse({'error': 'Unauthorized'}, status=403)

        try:
            body = json.loads(request.body) if request.body else {}
        except Exception:
            body = {}
        test_email = body.get('test_email', '')

        presave_url = "https://link.ghostpavilion.com/black-armor"
        subject = 'Pre-save the new single, "Black Armor"'

        if test_email:
            from collections import namedtuple
            FakeSub = namedtuple('FakeSub', ['email', 'unsubscribe_token'])
            subscribers = [FakeSub(email=test_email, unsubscribe_token='test')]
        else:
            subscribers = SignUp.objects.filter(is_subscribed=True, is_confirmed=True)

        total = len(subscribers) if test_email else subscribers.count()
        sent = 0
        failed = 0
        errors = []

        for subscriber in subscribers:
            unsubscribe_url = f"https://ghostpavilion2025-production.up.railway.app/unsubscribe/{subscriber.unsubscribe_token}/"

            html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body style="margin:0;padding:0;font-family:Verdana,Arial,sans-serif;background-color:#ffffff;">
  <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin:0;padding:0;background-color:#ffffff;">
    <tr><td style="padding:40px 20px;">
      <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width:600px;margin:0 auto;background-color:#ffffff;border-radius:8px;overflow:hidden;border:1px solid #e0e0e0;">
        <tr><td style="padding:40px 30px;text-align:center;background-color:#222222;">
          <h1 style="margin:0;color:#ffffff;font-size:36px;font-weight:bold;letter-spacing:4px;text-transform:uppercase;font-family:'Impact','Arial Black',Verdana,sans-serif;">GHOST PAVILION</h1>
        </td></tr>
        <tr><td style="padding:40px 30px;color:#222222;font-family:Verdana,Arial,sans-serif;font-size:16px;line-height:1.8;text-align:center;">
          <p style="margin:0 0 25px 0;text-align:center;">I have a new single coming out called <strong>&ldquo;Black Armor&rdquo;</strong>.</p>
          <p style="margin:0 0 25px 0;text-align:center;">Pre-save it now. When you do, it drops into your library automatically on release day and those day-one streams are what push it to new listeners.</p>
          <p style="margin:0 0 25px 0;text-align:center;">No labels. Just you and the music.</p>
          <p style="margin:0 0 25px 0;text-align:center;">
            <a href="{presave_url}" style="display:inline-block;background-color:#222222;color:#ffffff;padding:14px 40px;font-size:14px;font-weight:bold;text-decoration:none;border-radius:4px;letter-spacing:2px;text-transform:uppercase;font-family:Verdana,Arial,sans-serif;">PRE-SAVE NOW</a>
          </p>
          <p style="margin:0;text-align:center;">Thank you for being here.</p>
        </td></tr>
        <tr><td style="padding:30px;text-align:center;background-color:#f5f5f5;border-top:2px solid #222222;">
          <p style="margin:0 0 10px 0;color:#555555;font-size:12px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">GHOST PAVILION &copy; 2026</p>
          <p style="margin:0 0 10px 0;color:#555555;font-size:12px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">
            <a href="https://ghostpavilion.com" style="color:#222222;text-decoration:none;">ghostpavilion.com</a>
          </p>
          <p style="margin:0;color:#888888;font-size:10px;letter-spacing:1px;font-family:Verdana,Arial,sans-serif;">
            <a href="{unsubscribe_url}" style="color:#888888;text-decoration:underline;">Unsubscribe</a>
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
