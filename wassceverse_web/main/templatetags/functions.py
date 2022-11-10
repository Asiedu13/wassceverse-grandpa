import base64
from django import template

register = template.Library()

@register.filter
def encode(value):
    # b = base64.b64encode(bytes(value, 'utf-8'))
    b = base64.b64encode(value)
    base64_str = b.decode('utf-8')
    return base64_str