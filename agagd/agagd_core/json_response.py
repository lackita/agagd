# taken from http://djangosnippets.org/snippets/154/
# used with permission (http://djangosnippets.org/about/tos/)

from django.core.serializers import json, serialize
from django.db.models.query import QuerySet
from django.http import HttpResponse
import json as python_json

class JsonResponse(HttpResponse):
    def __init__(self, object):
        if isinstance(object, QuerySet):
            content = serialize('json', object)
        else:
            content = python_json.dumps(
                object, indent=2, cls=json.DjangoJSONEncoder,
                ensure_ascii=False)
        super(JsonResponse, self).__init__(
            content, content_type='application/json')
