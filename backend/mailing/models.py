from django.db import models
import uuid

class SignUp(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    unsubscribe_token = models.UUIDField(default=uuid.uuid4, unique=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    def get_unsubscribe_url(self):
        return f"https://ghostpavilion.com/unsubscribe/{self.unsubscribe_token}"