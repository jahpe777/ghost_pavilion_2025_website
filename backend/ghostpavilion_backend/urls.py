from django.contrib import admin
from django.urls import path
from mailing.views import SignUpCreateView, UnsubscribeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', SignUpCreateView.as_view(), name='signup'),
    path('unsubscribe/<uuid:token>/', UnsubscribeView.as_view(), name='unsubscribe'),
]
