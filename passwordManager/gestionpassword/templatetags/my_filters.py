from django import template

register = template.Library()

@register.filter
def hide_password(password):
    return '●' * len(password)
