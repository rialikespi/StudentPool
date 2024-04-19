from django.contrib import admin
from .models import Note, Review

# Register your models here to view them on admin panel
# allowing us to modify and view them

admin.site.register(Note)
admin.site.register(Review)