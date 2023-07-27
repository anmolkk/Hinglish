from django import template

register = template.Library()

@register.filter
def check_tuple(value):
    if type(value) == tuple:
        return True
    else:
        return False
    
@register.filter
def check_list(value):
    if type(value) == list:
        return True
    else:
        return False


