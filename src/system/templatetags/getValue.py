from django import template
register = template.Library()

@register.simple_tag
def get_value(title, image):
    return title[image]