from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from mezzanine.core.fields import RichTextField

# Create your models here.

#class Snippet(models.Model):
#
#    title = models.CharField(max_length=100, editable=True)
#    content = HTMLField(editable=True)
#
#
#
#    class Meta:
#        verbose_name = _("Snippet")
#        verbose_name_plural = _("Snippets")
##        ordering = ("-created_at",)

class Snippet(models.Model):
    """
    TextField that stores HTML.
    """


    title = models.CharField(max_length=100, editable=True)
    
    content = RichTextField(_("Content"))


#    def clean(self, value, model_instance):
#        """
#        Remove potentially dangerous HTML tags and attributes.
#        """
#        from mezzanine.conf import settings
#        from mezzanine.core.defaults import (RICHTEXT_FILTER_LEVEL_NONE,
#                                             RICHTEXT_FILTER_LEVEL_LOW)
#        settings.use_editable()
#        if settings.RICHTEXT_FILTER_LEVEL == RICHTEXT_FILTER_LEVEL_NONE:
#            return value
#        tags = settings.RICHTEXT_ALLOWED_TAGS
#        attrs = settings.RICHTEXT_ALLOWED_ATTRIBUTES
#        styles = settings.RICHTEXT_ALLOWED_STYLES
#        if settings.RICHTEXT_FILTER_LEVEL == RICHTEXT_FILTER_LEVEL_LOW:
#            tags += LOW_FILTER_TAGS
#            attrs += LOW_FILTER_ATTRS
#        return clean(value, tags=tags, attributes=attrs, strip=True,
#                     strip_comments=False, styles=styles)
