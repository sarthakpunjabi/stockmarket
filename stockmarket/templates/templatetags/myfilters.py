from django import template
register = template.Library()

@register.filter
def get(mapping,key):
    return mapping.get(key,'')

def some(value):
    return value["author"]

register.filter("some",some)