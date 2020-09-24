from django import template
from django.shortcuts import reverse
register = template.Library()


@register.filter(is_safe=True)
def label_with_classes(value):
    return value.label_tag(attrs={'class': 'sr-only'})


@register.filter(is_sate=True)
def add_class(value):
    print(value)
    value.css_classes('form-control')
    print(value)
    return value


@register.inclusion_tag('blog/list_pagination.html')
def load_pagination(page_obj, s):
    previous_url = ''
    next_url = ''
    previous_number = ''
    next_number = ''
    if page_obj.has_next():
        next_number = page_obj.next_page_number()
        next_url = reverse('blog:articles_list', kwargs={'page': next_number})
    if page_obj.has_previous():
        previous_number = page_obj.previous_page_number()
        previous_url = reverse('blog:articles_list', kwargs={'page': previous_number})
    return {'previous_url': previous_url,
            'next_url': next_url,
            'page_obj': page_obj,
            'next_number': next_number,
            'previous_number': previous_number,
            's': s,
            }


