from .interfaces import IFrontendTheme
from zope.interface import alsoProvides

# Use plone.app.theming / Plone standard theme only for these domains,
# starting with:
NOTHEME_DOMAINS = (
    "admin",
    "cms",
)


def set_theme(obj, event):
    """Custom or defaul main template?

    Use the custom main template for all domains except admin.*‌ or cms.*.
    """
    request = event.request
    http_host = request.HTTP_HOST
    if not any((http_host.startswith(domain) for domain in NOTHEME_DOMAINS)):
        alsoProvides(request, IFrontendTheme)
