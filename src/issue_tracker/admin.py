from django.contrib import admin

from .models import Type
from .models import Status
from .models import Task

# Register your models here.
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Task)
