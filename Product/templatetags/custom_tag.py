from django import template
register=template.Library()

@register.simple_tag
def calculate_old_price(price, discount):
    old_price = price / ((100 - discount) / 100)
    return round(old_price, 2)

