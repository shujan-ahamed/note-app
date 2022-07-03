from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=15, blank=False, null=False)
    body = models.TextField(max_length=80, blank=False, null=False)
    created_on = models.DateTimeField(default=timezone.now)
    PUBLISH = (
    ("1", "Private"),
    ("2", "Public"),
    )
    publish_as = models.CharField(max_length= 30,
        choices = PUBLISH,
        default = 'Public'
        )
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-title"]