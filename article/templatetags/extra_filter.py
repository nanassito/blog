from django import template

register = template.Library()

@register.filter()
def custom_format(value):
    value = value.replace("\n\n", '</p><p>')
    value = value.replace("\r\n\r\n", '</p><p>')
    value = value.replace("\n", "<br/>")
    value = value.replace("\r\n", "<br/>")
    return value
