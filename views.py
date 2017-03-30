from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from DB_start.models import *
from django.template import RequestContext
from datetime import datetime




def artists(request):
   artists = Artist.objects.all()
   return render(
       request,
       'DB_start/artists.html',
       {'artists': artists}
   )
  # return render_to_response('DB_start/artists.html', {'artists': artists})


def artistdetails(request, name):
    output = '<html><head><title>' + name
    output += '</title></head><body><h1>' + name
    output += '</h1></body></html>'
    return HttpResponse(output)

def home(request):
    assert isinstance(request, HttpRequest)
    # return dictionary
    return render(
        request,
        'DB_start/index.html',
         context =
         {
             'title': 'Home Page',
             'year':datetime.now().year,
         },

    )

def index():
    return HttpResponse('<html><head><title>Hello Django!</title></head></html>')