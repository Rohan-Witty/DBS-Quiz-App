from django.contrib import admin

from .models import Question, Option, CorrectOption

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(CorrectOption)

