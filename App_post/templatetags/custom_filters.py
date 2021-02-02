from django import template

register = template.Library()

def range_filter(value):
    return value[0:500]+'.........'


def range_filter_filter(value):
    return value[0:20]+'-----'

register.filter('range_filter', range_filter)
register.filter('range_filter_filter', range_filter_filter)
