from hashlib import md5
from urllib.parse import urlencode
from django import template

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=128):
    # Optimize for Chinese
    url = "https://sdn.geekzu.org/avatar/"
    default = 'mm'
    return url + "%s?%s" % (md5(email.lower().encode("utf-8")).hexdigest(), urlencode({'d': default, 's': str(size)}))