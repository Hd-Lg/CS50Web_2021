from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

text = [ "Text 1", "Text 2", "Text 3" ]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(text[num - 1])
    else:
        raise Http404("No such section")