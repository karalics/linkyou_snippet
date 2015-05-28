from django.contrib import admin
from linkyou_snippet.models import Snippet

# Register your models here.

class SnippetAdmin(admin.ModelAdmin):

     list_display = ( 'title', 'id', 'content',  )

admin.site.register(Snippet, SnippetAdmin)
