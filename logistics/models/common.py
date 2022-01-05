from django.contrib.auth.models import User
from django.db import models


class Log(models.Model):

    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"""Log: {self.description} [{self.created_by.username}:{self.created_at}]"""
