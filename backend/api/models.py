from django.db import models

# Create your models here.


class Todo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
