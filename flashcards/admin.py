from re import sub
from django.contrib import admin
from .models import Flashcard, User, Subject
# Register your models here.

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Flashcard)