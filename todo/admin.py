from django.contrib import admin
from todo.models import Task, Tag, Comment


# Register your models here.
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Comment)
