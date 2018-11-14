from django.db import models
from django.contrib.auth.models import User


class Email(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    # user id and name
    author = models.ForeignKey("Author", on_delete="SET_NULL")


class Author(models.Model):
    emails = models.ForeignKey("Email", on_delete="CASCADE", related_name="emails")
    user = models.OneToOneField(User, on_delete="CASCADE")

    def __str__(self):
        return f"{self.user}"
