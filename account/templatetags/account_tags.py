from django import template
import hashlib
register = template.Library()


@register.filter(is_safe=True)
def label_with_classes(value):
    return value.label_tag(attrs={'class': 'sr-only'})


@register.filter(is_safe=True)
def gravatar(user, size=100, default='identicon', rating='g'):
    url = 'https://secure.gravatar.com/avatar'
    hash = user.avatar_hash or hashlib.md5(user.email.encode('utf-8')).hexdigest()
    return '{url}/{hash}?s={size}&d={default}&r=' \
           '{rating}'.format(url=url, hash=hash, size=size, default=default, rating=rating)