from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'create_todo$', views.create_todo),
    re_path(r'update_todo$', views.update_todo),
    re_path(r'get_todos$', views.get_todos),
    re_path(r'delete_todo$', views.delete_todo),
    re_path(r'create_log$', views.create_log),
    re_path(r'get_logs$', views.get_logs),
]
