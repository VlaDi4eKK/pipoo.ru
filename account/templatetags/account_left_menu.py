# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.inclusion_tag('templatetags/account_left_menu.html')
def account_left_menu():
    return {}