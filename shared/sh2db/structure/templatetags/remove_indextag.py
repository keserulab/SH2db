from django import template

register = template.Library()

@register.filter
def remove_indextag(value):
    return value.replace("$index","")