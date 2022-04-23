from django.contrib import admin
from .models import User, Polls

# Register your models here.

admin.site.site_header = "My Polls Admin"
admin.site.site_title = "My Polls"
# admin.site.index_title = "Welcome to the My Polls Admin Area"


class UserDisplay(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username", "email")


admin.site.register(User, UserDisplay)
admin.site.register(Polls)
