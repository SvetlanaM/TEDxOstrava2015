from django import template
from django.contrib.sites.models import RequestSite    

register = template.Library()

@register.simple_tag
def get_url():
    return RequestSite(request).domain