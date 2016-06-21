from django.db import models

# Create your models here.


class Chirp(models.Model):
    body = models.CharField(max_length=141)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    class Meta:
        ordering = ["-date"]
