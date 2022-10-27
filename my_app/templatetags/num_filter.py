from django import template

register = template.Library()

@register.filter
def number_sep(value):
	a = format(int(value), ',d').replace(',', ' ')
	return a