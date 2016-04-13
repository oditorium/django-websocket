from django.test import TestCase


from django.test import TestCase, RequestFactory
#from django.conf import settings
#from django.core.urlresolvers import reverse_lazy, reverse
#from Presmo.tools import ignore_failing_tests, ignore_long_tests

import json

from . import websock as ws
from .websock import __version__
from . import views as v

VERSION = "0.0"

#########################################################################################
## BASE TEST
class BaseTest(TestCase):
    
    def setUp(s):
        s.factory = RequestFactory()
        s.req_get  = s.factory.get ('/url/does/not/matter', {})
        s.req_post = s.factory.post('/url/does/not/matter', {})

    def test_version(s):
        s.assertEqual (__version__, VERSION)
        resp = v.version(s.req_get)
        s.assertEqual (json.loads(resp.content.decode())['version'], VERSION)


    