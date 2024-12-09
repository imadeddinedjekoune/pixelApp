from django.db import models

class PixelTrackerRequest(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)  # When the request was made
    ip_address = models.GenericIPAddressField(null=True, blank=True)  # Client's IP address
    user_agent = models.TextField(null=True, blank=True)  # Client's user agent
    msg_id = models.CharField(max_length=255, null=True, blank=True)  # Message ID for tracking

    def __str__(self):
        return f"Request at {self.timestamp} from {self.ip_address} (msg_id: {self.msg_id})"
