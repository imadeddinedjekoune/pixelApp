from django.contrib import admin
from .models import PixelTrackerRequest

@admin.register(PixelTrackerRequest)
class PixelTrackerRequestAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address', 'user_agent','msg_id')
    list_filter = ('timestamp','msg_id')
    search_fields = ('ip_address', 'user_agent','msg_id')
