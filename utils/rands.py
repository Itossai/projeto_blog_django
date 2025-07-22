import string
from random import SystemRandom
from django.utils.text import slugify

def random_letters(size=5):
    return ''.join(SystemRandom().choices(
        string.ascii_letters+string.digits,
        k=size
    ))


def new_slugfy(text,size=5):
    return slugify(text)+'-'+random_letters(size)
