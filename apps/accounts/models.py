from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    email_address = models.EmailField(blank=True)
    password = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_active_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    @property
    def username(self):
        return f"user{self.id}"

    def __str__(self):
        return self.username

