from django.db import models
from django.utils import timezone


class LastTweetID(models.Model):
    time = models.DateTimeField(default=timezone.now)
    tweetId=models.CharField(max_length=100)


    def __str__(self):
        return str(self.time)