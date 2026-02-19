from django.contrib import admin
from django.urls import path
from mailing.views import SignUpCreateView, UnsubscribeView, SendMassEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignUpCreateView.as_view(), name='signup'),
    path('unsubscribe/<uuid:token>/', UnsubscribeView.as_view(), name='unsubscribe'),
    path('api/send-mass-email/', SendMassEmailView.as_view(), name='send-mass-email'),
]
