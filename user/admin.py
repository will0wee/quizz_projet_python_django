from django.contrib import admin
from .models import User_type, User_data

class User_dataAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')
    list_filter = ('user', 'user_type',)
    ordering = ('user', 'user_type')
    search_fields = ('user', 'user_type')

admin.site.register(User_type)
admin.site.register(User_data, User_dataAdmin)
