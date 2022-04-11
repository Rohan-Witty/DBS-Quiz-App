from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Question, Option, CorrectOption

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(CorrectOption)

