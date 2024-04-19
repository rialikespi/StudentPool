from django.contrib import admin
from .models import  Question, Module, User, Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Module)
admin.site.register(User)
admin.site.register(Answer)