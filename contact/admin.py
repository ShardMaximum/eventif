from django.contrib import admin
from contact.models import Message

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'created_at', 'response', 'response_date']
    date_hierarchy = 'created_at'
    search_fields = ['name', 'email', 'phone', 'message', 'created_at', 'response', 'response_date']
    list_filter = ['email','created_at','response_date']

admin.site.register(Message, ContactModelAdmin)