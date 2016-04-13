#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.http import Http404

from . import websock as ws

################################################################################
## VERSION page - version information
from .websock import __version__ as _ver, __version_dt__ as _ver_dt, __name__ as _nam
def version(request):
    data = {
        'app': _nam.split('.')[0],
        'library': _nam.split('.')[-1],
        'library_full': _nam,
        'version': _ver,
        'version_dt': _ver_dt,
    }
    return JsonResponse (data)
