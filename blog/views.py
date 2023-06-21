from django.shortcuts import render
from django.http import Http404


def notFound(request):
    raise Http404

def bad_request(request, exception, template_name='blog/404.html'):
 return render(request, template_name)

def permission_denied(request, exception, template_name='blog/404.html'):
 return render(request, template_name)
 
def page_not_found(request, exception, template_name='blog/404.html'):
 return render(request, template_name)
 
def server_error(request, template_name='blog/404.html'):
 return render(request, template_name)
