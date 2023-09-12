from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)


class Logs(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user_action = models.CharField(max_length=255)
