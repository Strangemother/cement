"""
   {% timedelta cart.updated cart.created format="" %}
   {{ cart.created|timesince:cart.updated }}
   {% human_timedelta cart.updated cart.created format="" %}
"""
from django import template
from datetime import timedelta
from django.urls import reverse
from django.utils.translation import ngettext

register = template.Library()



@register.simple_tag(takes_context=False)
def str_merge(*targs, **kwargs):
    """Concatenate many items as a stringy merge, each item is cast
    as str() before the join:

        {% str_merge "images/" forloop.counter '.png' as iurl %}
        {{ iurl }}

        "images/1.png"
    """
    return ''.join(map(str, targs))
