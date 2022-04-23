from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from datetime import datetime
import pytz

tz = pytz.timezone("Asia/Calcutta")


class User(AbstractUser):
    token = models.UUIDField(default=uuid4, editable=False, unique=True)
    token_date = models.DateTimeField(
        default=datetime.now(tz=tz), editable=True)


class Polls(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choices = models.ManyToManyField(
        'Choices', blank=True, related_name="poll_choices")

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "active": self.active,
            "user": self.user.id,
            "choices": [choice.title for choice in self.choices.all()]
        }


class Choices(models.Model):
    title = models.CharField(max_length=120)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(
        Polls, on_delete=models.CASCADE, related_name="choice_parent")
    users = models.ManyToManyField(
        "User", blank=True, related_name="choice_users")

    def __str__(self):
        return str(self.id)+self.title

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "votes": self.votes,
            "poll": self.poll.id,
            "users": [user.id for user in self.users.all()]
        }
