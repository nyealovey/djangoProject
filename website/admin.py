from django.contrib import admin

# Register your models here.
from website.models import Topic
from website.models import Entry

admin.site.register(Topic)
admin.site.register(Entry)

