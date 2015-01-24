from django.contrib import admin

from models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('when', 'owner', 'content')

admin.site.register(Message, MessageAdmin)