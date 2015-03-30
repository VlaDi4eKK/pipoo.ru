# -*- coding: utf-8 -*-
from django import template
from catalog.models import Category
register = template.Library()

@register.inclusion_tag('templatetags/catalog_left_menu.html')
def catalog_left_menu(parent, child):
    parents = Category.objects.filter(parent=None)
    for parent_one in parents:
        parent_one.categories = Category.objects.filter(parent=parent_one)
    return {'categories': parents, 'parent': parent, 'child': child}
