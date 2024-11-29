import datetime
from django import template 
from genedata.models import Gene

register = template.Library()

@register.simple_tag
def todays_date():
    return datetime.datetime.now().strftime('%d %b %Y')

@register.simple_tag
def author_name():
    return "Paffcio"

@register.simple_tag
def gene_count():
    return Gene.objects.count()