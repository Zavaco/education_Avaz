from django import template
from ..models import Course


register = template.Library()


@register.simple_tag
def get_footer():
    return Course.objects.all()


