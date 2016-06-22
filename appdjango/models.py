from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Chirp(models.Model):
    body = models.CharField(max_length=141)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    class Meta:
        ordering = ["-date"]


class StopWord(models.Model):
    word = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField("auth.user")
    favorite_bird = models.CharField(max_length=100, null=True)


@receiver(post_save, sender=StopWord)
# post_save = signal, sender = Class
def say_hello(**kwargs):
    print('Hello world')


@receiver(post_save, sender='auth.user')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)
# this will be set off every time the post_save is called within a view
# instance referse to the model.object that was just generated
