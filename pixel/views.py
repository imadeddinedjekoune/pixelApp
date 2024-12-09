from django.http import HttpResponse
from .models import PixelTrackerRequest

def pixel_tracker(request):
    # Extract request details
    ip_address = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
    msg_id = request.GET.get('msg_id')  # Extract msg_id from query parameters

    # Save to the database
    PixelTrackerRequest.objects.create(ip_address=ip_address, user_agent=user_agent, msg_id=msg_id)

    # Serve a 1x1 transparent GIF
    pixel_gif = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
    response = HttpResponse(pixel_gif, content_type="image/gif")
    return response

def get_client_ip(request):
    """Get the client IP address from the request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
