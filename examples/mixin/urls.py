from olddjangorestframework.compat import View  # Use Django 1.3's django.views.generic.View, or fall back to a clone of that if Django < 1.3
from olddjangorestframework.mixins import ResponseMixin
from olddjangorestframework.renderers import DEFAULT_RENDERERS
from olddjangorestframework.response import Response
from olddjangorestframework.reverse import reverse

from django.conf.urls.defaults import patterns, url


class ExampleView(ResponseMixin, View):
    """An example view using Django 1.3's class based views.
    Uses olddjangorestframework's RendererMixin to provide support for multiple
    output formats."""
    renderers = DEFAULT_RENDERERS

    def get(self, request):
        url = reverse('mixin-view', request=request)
        response = Response(200, {'description': 'Some example content',
                                  'url': url})
        return self.render(response)


urlpatterns = patterns('',
    url(r'^$', ExampleView.as_view(), name='mixin-view'),
)
