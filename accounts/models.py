import string
import secrets

from django.db import models

def create_password():
    choices = string.ascii_letters + string.digits
    return ''.join(secrets.choice(choices) for character in range(12))

class User(models.Model):
    email_address = models.EmailField(blank=True)
    password = models.CharField(max_length=255, default=create_password)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_active_date = models.DateTimeField(auto_now=True)

    @property
    def username(self):
        return f"user{self.id}"

