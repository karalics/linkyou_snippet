from django.shortcuts import render
from linkyou_snippet.models import Snippet

# Create your views here.

def snippet_view(request):
     snippet_list = Snippet.objects.all()
     context = {'snippet_list' : snippet_list}
     return render(request, 'snippet/snippet.html', context)
