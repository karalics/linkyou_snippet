from linkyou_snippet.models import Snippet
from mezzanine import template

register = template.Library()

@register.as_tag
def snippet_list(*args):

    snippets = Snippet.objects.all()
    return list(snippets) 
