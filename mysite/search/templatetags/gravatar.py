import os
import random
import posixpath
from hashlib import md5
from urllib.parse import urlencode
from django import template
from django.conf import settings

register = template.Library()

# return only the URL of the gravatar
# TEMPLATE USE:  {{ email|gravatar_url:150 }}
@register.filter
def gravatar_url(email, size=128):
    # Optimize for Chinese
    url = "https://sdn.geekzu.org/avatar/"
    default = 'mm'
    return url + "%s?%s" % (md5(email.lower().encode("utf-8")).hexdigest(), urlencode({'d': default, 's': str(size)}))

def is_image_file(filename):
    """Does `filename` appear to be an image file?"""
    img_types = [".jpg", ".jpeg", ".png", ".gif"]
    ext = os.path.splitext(filename)[1].lower()
    return ext in img_types

@register.simple_tag
def random_img(path):
    """
    Select a random image file from the provided directory
    and return its href. `path` should be relative to MEDIA_ROOT.
    Usage:  <img src='{% random_image "images/whatever/" %}'>
    """
    fullpath = os.path.join(settings.MEDIA_ROOT, path)
    filenames = [f for f in os.listdir(fullpath) if is_image_file(f)]
    pick = random.choice(filenames)
    return posixpath.join(settings.MEDIA_URL, path, pick)