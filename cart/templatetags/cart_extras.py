from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def multiply(value, arg):
    if value is None:
        value = Decimal('0.00')
    return value * arg
