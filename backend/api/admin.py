from django.contrib import admin
from .models import Todo, Logs

# Register your models here.
admin.site.register(Todo)
admin.site.register(Logs)
