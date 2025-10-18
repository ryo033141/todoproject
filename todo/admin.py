from django.contrib import admin
from .models import TodoModel

# TodoModelを管理画面に表示
admin.site.register(TodoModel)
