from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):            
    return render_to_response('main/home.html', {},
                              context_instance=RequestContext(request))
    
def test(request): 
    if request.method == 'GET':      
        print "Works"
        return HttpResponse("Yahooooooooooooo!!!!!!!!!!!!!!!")