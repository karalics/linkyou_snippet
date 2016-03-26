from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import RichTextField



class Snippet(models.Model):
    """
    TextField that stores HTML.
    """


    title = models.CharField(max_length=100, editable=True)
    
    content = RichTextField(_("Sadrzaj"), editable=True)
    is_activated = BooleanField(_("Aktivirano"), default=True)
    is_warning = BooleanField(_("Vazno Obavjestenje"), default=False)




