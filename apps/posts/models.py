from django.db import models

class Posts(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["creation_date"]

    def __str__(self):
        return f"{self.title[:10]}.. {self.user}"